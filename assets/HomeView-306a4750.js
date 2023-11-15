import{_ as V,c as y,s as w,a as U,h as k,b as z,d as q,p as O,e as j,f as x,r as f,o as _,g as p,i as s,j as t,k as u,w as l,l as v,v as g,F as m,m as b,n as C,t as h,q as A,u as S}from"./index-2aa79ce7.js";const E="/Cheq/assets/urban-74f20a8f.png",I="/Cheq/assets/vestir-bfed8197.png",L="/Cheq/assets/camperaU-7c7091c0.jpg",T="/Cheq/assets/buzoU-7b8e4622.jpg",N="/Cheq/assets/remeraU-f097f531.jpg",P="/Cheq/assets/pantalonU-484b86c5.jpg",B="/Cheq/assets/camperaV-432fac61.jpg",F="/Cheq/assets/buzoV-e9628677.jpg",H="/Cheq/assets/camisaV-c4a19591.jpg",M="/Cheq/assets/pantalonV-93a8488e.jpg";const R={data(){return{card:y,sync:w,checkmarkCircle:U,helpCircle:k,storefront:z,cube:q,pin:O,searchSharp:j,close:x,productosV:[],productosU:[],yOffsetU:null,yOffsetV:null,searchU:"",searchV:""}},computed:{filteredProductosU(){return this.productosU.filter(c=>c.nombre.toLowerCase().includes(this.searchU.toLowerCase()))},filteredProductosV(){return this.productosV.filter(c=>c.nombre.toLowerCase().includes(this.searchV.toLowerCase()))}},methods:{viewUrban(){this.yOffsetU=45},viewVestir(){this.yOffsetV=45},closeArt(){this.yOffsetU=-150,this.yOffsetV=-150}},mounted(){fetch("http://127.0.0.1:5000/productos").then(c=>{if(c.ok)return c.json();throw new Error("Error al obtener los datos de los productos")}).then(c=>{this.productosU=c.filter(a=>a.tipo==="Urban"),this.productosV=c.filter(a=>a.tipo==="Vestir")}).catch(c=>{console.error("Error:",c)})}},e=c=>(A("data-v-81ae2c8c"),c=c(),S(),c),D={class:"enlaces"},Z=e(()=>s("h2",null,"Colección invierno",-1)),G=e(()=>s("span",null,"buzos,",-1)),Y=e(()=>s("span",null,"camperas,",-1)),J=e(()=>s("span",null,"remeras,",-1)),K=e(()=>s("span",null,"pantalones",-1)),Q=e(()=>s("span",null,"camisas.",-1)),W={class:"order-search"},X={class:"search"},$={class:"articulos urban"},ss=["src"],es={class:"detail"},ts={class:"enlaces"},os=e(()=>s("h2",null,"Colección invierno",-1)),ns=e(()=>s("span",null,"buzos,",-1)),ls=e(()=>s("span",null,"camperas,",-1)),as=e(()=>s("span",null,"remeras,",-1)),is=e(()=>s("span",null,"pantalones",-1)),cs=e(()=>s("span",null,"camisas.",-1)),rs={class:"order-search"},ds={class:"search"},us={class:"articulos vestir"},_s=["src"],ps={class:"detail"},hs={class:"main"},ms={class:"inicio"},fs={class:"names"},vs={class:"Che"},gs={class:"eq"},bs=e(()=>s("img",{src:E,alt:"Ropa urbana",class:"casual"},null,-1)),Cs=[bs],Vs=e(()=>s("img",{src:I,alt:"Ropa de vestir",class:"evento"},null,-1)),ys=[Vs],ws={class:"catalogo"},Us=e(()=>s("h2",null,"CATALOGO",-1)),ks={class:"grid-container"},zs={class:"grid-item"},qs=e(()=>s("img",{src:L,alt:"campera"},null,-1)),Os={class:"grid-item"},js=e(()=>s("img",{src:T,alt:"buzos"},null,-1)),xs={class:"grid-item"},As=e(()=>s("img",{src:N,alt:"remeras"},null,-1)),Ss={class:"grid-item"},Es=e(()=>s("img",{src:P,alt:"pantalones"},null,-1)),Is={class:"grid-item"},Ls=e(()=>s("img",{src:B,alt:"camperas"},null,-1)),Ts={class:"grid-item"},Ns=e(()=>s("img",{src:F,alt:"buzos"},null,-1)),Ps={class:"grid-item"},Bs=e(()=>s("img",{src:H,alt:"camisas"},null,-1)),Fs={class:"grid-item"},Hs=e(()=>s("img",{src:M,alt:"pantalones"},null,-1)),Ms=e(()=>s("div",{class:"container-pagos"},[s("div",{class:"tres-cuotas"},[s("p",null,"3"),s("p",null,"Cuotas sin interes")]),s("span"),s("div",{class:"seis-cuotas"},[s("p",null,"6"),s("p",null,"Cuotas sin interes")])],-1)),Rs={class:"info"},Ds=e(()=>s("h4",null,"Envio gratis a todo el pais",-1)),Zs=e(()=>s("p",null,"en compras superiores a $25.000",-1)),Gs={class:"store"},Ys=e(()=>s("h4",null,"Retiro en tienda",-1)),Js=e(()=>s("p",null,"Elegí tu tienda más cercana",-1)),Ks=e(()=>s("h4",null,"¿Necesitas ayuda?",-1)),Qs=e(()=>s("p",null,"Aclará todas tus dudas o consultas",-1)),Ws=e(()=>s("h4",null,"Compra 100% segura",-1)),Xs=e(()=>s("p",null,"Tu información protegida y garantizada",-1)),$s={class:"card"},se=e(()=>s("h4",null,"Financiación",-1)),ee=e(()=>s("p",null,"Conocé las promociones bancarias",-1)),te=e(()=>s("h4",null,"Cambios",-1)),oe=e(()=>s("p",null,"Hasta 30 días después de la compra",-1)),ne=e(()=>s("p",null,"Encontranos en todos estos locales",-1)),le=e(()=>s("iframe",{src:"https://www.youtube-nocookie.com/embed/OaVsCM0Zeio?modestbranding=1&controls=0&mute=1&autoplay=1&disablekb=1&loop=1&playlist=OaVsCM0Zeio&rel=0&showinfo=0",title:"YouTube video player",frameborder:"0",allow:"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"},`
            `,-1));function ae(c,a,ie,ce,i,r){const d=f("ion-icon"),n=f("router-link");return _(),p(m,null,[s("div",{class:"ventana urban-catalogo",style:C({top:i.yOffsetU+"%"})},[s("span",{class:"cruz cruzU",onClick:a[0]||(a[0]=(...o)=>r.closeArt&&r.closeArt(...o))},[t(d,{src:i.close},null,8,["src"])]),s("div",D,[Z,s("p",null,[u("Visita tambien nuestros "),t(n,{to:{name:"buzos"}},{default:l(()=>[G]),_:1}),t(n,{to:{name:"camperas"}},{default:l(()=>[Y]),_:1}),t(n,{to:{name:"remeras"}},{default:l(()=>[J]),_:1}),t(n,{to:{name:"pantalones"}},{default:l(()=>[K]),_:1}),u(" o "),t(n,{to:{name:"camisas"}},{default:l(()=>[Q]),_:1})])]),s("div",W,[s("div",X,[t(d,{src:i.searchSharp},null,8,["src"]),v(s("input",{type:"text","onUpdate:modelValue":a[1]||(a[1]=o=>i.searchU=o)},null,512),[[g,i.searchU]])])]),s("div",$,[(_(!0),p(m,null,b(r.filteredProductosU,o=>(_(),p("div",{key:o.id},[s("div",null,[s("img",{src:o.url_Image,alt:"Articulo"},null,8,ss),s("h4",null,h(o.nombre),1),s("p",null,"$"+h(o.precio),1),s("div",es,[t(n,{to:{name:"product-detail",params:{id:o.id}}},{default:l(()=>[u(" Ver ")]),_:2},1032,["to"])])])]))),128))])],4),s("div",{class:"ventana vestir-catalogo",style:C({top:i.yOffsetV+"%"})},[s("span",{class:"cruz cruzV",onClick:a[2]||(a[2]=(...o)=>r.closeArt&&r.closeArt(...o))},[t(d,{src:i.close},null,8,["src"])]),s("div",ts,[os,s("p",null,[u("Visita tambien nuestros "),t(n,{to:{name:"buzos"}},{default:l(()=>[ns]),_:1}),t(n,{to:{name:"camperas"}},{default:l(()=>[ls]),_:1}),t(n,{to:{name:"remeras"}},{default:l(()=>[as]),_:1}),t(n,{to:{name:"pantalones"}},{default:l(()=>[is]),_:1}),u(" o "),t(n,{to:{name:"camisas"}},{default:l(()=>[cs]),_:1})])]),s("div",rs,[s("div",ds,[t(d,{src:i.searchSharp},null,8,["src"]),v(s("input",{type:"text","onUpdate:modelValue":a[3]||(a[3]=o=>i.searchV=o)},null,512),[[g,i.searchV]])])]),s("div",us,[(_(!0),p(m,null,b(r.filteredProductosV,o=>(_(),p("div",{key:o.id},[s("div",null,[s("img",{src:o.url_Image,alt:"Articulo"},null,8,_s),s("h4",null,h(o.nombre),1),s("p",null,"$"+h(o.precio),1),s("div",ps,[t(n,{to:{name:"product-detail",params:{id:o.id}}},{default:l(()=>[u(" Ver ")]),_:2},1032,["to"])])])]))),128))])],4),s("main",hs,[s("section",null,[s("div",ms,[s("div",fs,[s("div",vs,[s("h1",{class:"name1",onClick:a[4]||(a[4]=(...o)=>r.viewUrban&&r.viewUrban(...o))},"Ch")]),s("div",gs,[s("h1",{class:"name2",onClick:a[5]||(a[5]=(...o)=>r.viewVestir&&r.viewVestir(...o))},"eq")])]),s("div",{class:"gray",onClick:a[6]||(a[6]=(...o)=>r.viewUrban&&r.viewUrban(...o))},Cs),s("div",{class:"lightblue",onClick:a[7]||(a[7]=(...o)=>r.viewVestir&&r.viewVestir(...o))},ys)])]),s("section",ws,[Us,s("div",ks,[s("div",zs,[s("figure",null,[t(n,{to:{name:"camperas"}},{default:l(()=>[qs]),_:1})])]),s("div",Os,[s("figure",null,[t(n,{to:{name:"buzos"}},{default:l(()=>[js]),_:1})])]),s("div",xs,[s("figure",null,[t(n,{to:{name:"remeras"}},{default:l(()=>[As]),_:1})])]),s("div",Ss,[s("figure",null,[t(n,{to:{name:"pantalones"}},{default:l(()=>[Es]),_:1})])]),s("div",Is,[s("figure",null,[t(n,{to:{name:"camperas"}},{default:l(()=>[Ls]),_:1})])]),s("div",Ts,[s("figure",null,[t(n,{to:{name:"buzos"}},{default:l(()=>[Ns]),_:1})])]),s("div",Ps,[s("figure",null,[t(n,{to:{name:"camisas"}},{default:l(()=>[Bs]),_:1})])]),s("div",Fs,[s("figure",null,[t(n,{to:{name:"pantalones"}},{default:l(()=>[Hs]),_:1})])])]),Ms,s("div",Rs,[s("div",null,[t(d,{src:i.cube},null,8,["src"]),Ds,Zs]),s("div",Gs,[t(d,{src:i.storefront},null,8,["src"]),Ys,Js]),s("div",null,[t(d,{src:i.helpCircle},null,8,["src"]),Ks,Qs]),s("div",null,[t(d,{src:i.checkmarkCircle},null,8,["src"]),Ws,Xs]),s("div",$s,[t(d,{src:i.card},null,8,["src"]),se,ee]),s("div",null,[t(d,{src:i.sync},null,8,["src"]),te,oe])]),t(n,{to:{name:"about"},class:"extra"},{default:l(()=>[t(d,{src:i.pin},null,8,["src"]),ne]),_:1}),le])])],64)}const de=V(R,[["render",ae],["__scopeId","data-v-81ae2c8c"]]);export{de as default};
