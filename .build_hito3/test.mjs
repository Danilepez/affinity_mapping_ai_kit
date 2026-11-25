import fs from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
const runtime='C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1123-915-0_26.1123.915.0_x64__3k8sg7r9htsxt/dependencies';
const {Presentation,PresentationFile}=await import(pathToFileURL(runtime+'/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs').href);
const p=Presentation.create({slideSize:{width:1280,height:720}});
const s=p.slides.add();s.background.fill='#F5F2EA';
let t=s.shapes.add({geometry:'textbox',position:{left:70,top:100,width:1100,height:200},fill:'none',line:{fill:'none',width:0}});t.text='Qhatu';t.text.style={fontFamily:'Arial',fontSize:64,bold:true,color:'#153E3B'};
await fs.writeFile('.build_hito3/test.png',new Uint8Array(await (await p.export({slide:s,format:'png',scale:1})).arrayBuffer()));
console.log('render ok');
