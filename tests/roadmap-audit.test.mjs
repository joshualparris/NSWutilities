import test from "node:test";
import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";

async function load(relative) {return JSON.parse(await readFile(new URL(relative, import.meta.url),"utf8"))}
test("all 16 RT-SYS designations retain unique permanent IDs",async()=>{
 const reg=await load("../docs/UTILITY_SYSTEM_REGISTER.json");
 const audit=await load("../docs/UTILITY_ROADMAP_AUDIT_2026-10-25.json");
 assert.equal(reg.systems.length,16);assert.equal(audit.systems.length,16);
 assert.equal(new Set(reg.systems.map(x=>x.id)).size,16);
 assert.deepEqual(reg.systems.map(x=>x.id),audit.systems.map(x=>x.id));
 const dedicated=audit.systems.filter(x=>x.roadmapStatus==="dedicated");
 assert.equal(dedicated.length,4);
 assert.deepEqual(dedicated.map(x=>x.id),["RT-SYS-001","RT-SYS-002","RT-SYS-003","RT-SYS-004"]);
 assert.equal(audit.completeDedicatedCount,4);
 assert.equal(audit.notVerifiedDedicatedCount,12);
 assert.equal(audit.nextRecommendedSystem,"RT-SYS-005");
});
test("RTSM-001 to RTSM-030 stable, unique, valid dependency DAG",async()=>{
 const {tasks,triageOrder,systemId}=await load("../docs/STORMWATER_TASKS.json");
 assert.equal(systemId,"RT-SYS-004");assert.equal(tasks.length,30);
 const ids=tasks.map(x=>x.id);
 assert.deepEqual(ids,Array.from({length:30},(_,i)=>"RTSM-"+String(i+1).padStart(3,"0")));
 const all=new Set(ids);assert.equal(all.size,30);
 for(const t of tasks){
  assert.ok(["P0","P1","P2"].includes(t.priority));
  assert.ok(["open","research-doc-complete"].includes(t.status));
  assert.ok(typeof t.acceptance==="string"&&t.acceptance.length>35);
  assert.ok(typeof t.parent==="string"&&t.parent.includes("RTU-"));
  for(const d of t.dependsOn)assert.ok(all.has(d),t.id+" invalid dependency "+d);
 }
 const closed=new Set(tasks.filter(x=>x.status==="research-doc-complete").map(x=>x.id));
 assert.deepEqual(triageOrder.length,28);
 for(const taskId of triageOrder){
  const task=tasks.find(x=>x.id===taskId);
  assert.ok(!closed.has(taskId),taskId+" repeated");
  assert.ok(task.dependsOn.every(d=>closed.has(d)),taskId+" dependencies not ready");
  closed.add(taskId);
 }
 assert.equal(closed.size,30);
});
test("research tasks documented, runtime tasks remain open",async()=>{
 const {tasks,nextUnblockedTasks}=await load("../docs/STORMWATER_TASKS.json");
 assert.deepEqual(tasks.filter(x=>x.status==="research-doc-complete").map(x=>x.id),["RTSM-001","RTSM-002"]);
 assert.deepEqual([...nextUnblockedTasks].sort(),["RTSM-003","RTSM-004","RTSM-007"].sort());
 assert.ok(tasks.slice(2).every(x=>x.status==="open"));
});
