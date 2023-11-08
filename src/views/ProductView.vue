<template>
    <div class="wrapper-producto">
        <div class="image-producto">
            <figure class="primary">
                <img :src="product.url_Image" alt="Producto">
            </figure>
            <div>
                <p></p>
            </div>
        </div>
        <div class="datos-producto">
            <div class="nombre-producto">
                <h2>{{ product.nombre }}</h2>
            </div>
            <div class="valor-producto">
                <h2>${{ product.precio }}</h2>
            </div>
            <div class="cantidad-producto">
                <span class="decremento" @click="decrementCantidad" :disabled="count === 1">-</span>
                <span class="valor-cantidad">{{ count }}</span>
                <span class="incremento" @click="incrementCantidad" :disabled="count === cantidadDisponible">+</span>
            </div>
            <div class="info-producto">
                <h3>Cantidad de stock</h3>
                <div>
                    <span :style="stockColor(product.stock)">
                        {{ getStockStatus(product.stock) }}
                    </span>
                </div>
            </div>
            <div class="info-talle">
                <h3>Talle</h3>
                <div class="span-talle">
                    <span :class="{available : product.XS, selected : selectedTalle == 'XS'}" @click="selectTalla('XS')">38</span>
                    <span :class="{available : product.S, selected : selectedTalle == 'S'}" @click="selectTalla('S')">40</span>
                    <span :class="{available : product.M, selected : selectedTalle == 'M'}" @click="selectTalla('M')">42</span>
                    <span :class="{available : product.L, selected : selectedTalle == 'L'}" @click="selectTalla('L')">44</span>
                    <span :class="{available : product.XL, selected : selectedTalle == 'XL'}" @click="selectTalla('XL')">46</span>
                    <span :class="{available : product.XXL, selected : selectedTalle == 'XXL'}" @click="selectTalla('XXL')">48</span>
                </div>
            </div>
            <div class="title-medidas">
                <h3>Medidas</h3>
            </div>
            <div class="medidas">
                <div v-show="chooseMedidas === 'pantalon'">
                    <h4>Pantalón</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Talle</th>
                                <th>38</th>
                                <th>40</th>
                                <th>42</th>
                                <th>44</th>
                                <th>46</th>
                                <th>48</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Cintura</td>
                                <td>37</td>
                                <td>38</td>
                                <td>39</td>
                                <td>41.5</td>
                                <td>43</td>
                                <td>44</td>
                            </tr>
                            <tr>
                                <td>Largo Total</td>
                                <td>108.5</td>
                                <td>109.5</td>
                                <td>110.5</td>
                                <td>111.5</td>
                                <td>113</td>
                                <td>114</td>
                            </tr>
                            <tr>
                                <td>Tiro Delantero</td>
                                <td>30</td>
                                <td>30</td>
                                <td>30</td>
                                <td>30.5</td>
                                <td>31.5</td>
                                <td>31.5</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-show="chooseMedidas === 'remeraO'">
                    <h4>Remera Oversize</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Talle</th>
                                <th>38</th>
                                <th>40</th>
                                <th>42</th>
                                <th>44</th>
                                <th>46</th>
                                <th>48</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Ancho</td>
                                <td>45</td>
                                <td>47</td>
                                <td>49</td>
                                <td>51</td>
                                <td>53</td>
                                <td>55</td>
                            </tr>
                            <tr>
                                <td>Largo</td>
                                <td>70</td>
                                <td>72</td>
                                <td>74</td>
                                <td>76</td>
                                <td>78</td>
                                <td>80</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-show="chooseMedidas === 'remeraV'">
                    <h4>Remera Vestir</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Talle</th>
                                <th>38</th>
                                <th>40</th>
                                <th>42</th>
                                <th>44</th>
                                <th>46</th>
                                <th>48</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Ancho</td>
                                <td>41</td>
                                <td>43</td>
                                <td>45</td>
                                <td>47</td>
                                <td>49</td>
                                <td>51</td>
                            </tr>
                            <tr>
                                <td>Largo</td>
                                <td>64</td>
                                <td>66</td>
                                <td>68</td>
                                <td>70</td>
                                <td>72</td>
                                <td>74</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-show="chooseMedidas === 'buzo'">
                    <h4>Buzo</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Talle</th>
                                <th>38</th>
                                <th>40</th>
                                <th>42</th>
                                <th>44</th>
                                <th>46</th>
                                <th>48</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Ancho</td>
                                <td>51</td>
                                <td>53</td>
                                <td>55</td>
                                <td>57</td>
                                <td>59</td>
                                <td>61</td>
                            </tr>
                            <tr>
                                <td>Largo</td>
                                <td>66</td>
                                <td>68</td>
                                <td>70</td>
                                <td>72</td>
                                <td>74</td>
                                <td>76</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-show="chooseMedidas === 'camisa'">
                    <h4>Camisa</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Talle</th>
                                <th>38</th>
                                <th>40</th>
                                <th>42</th>
                                <th>44</th>
                                <th>46</th>
                                <th>48</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Contorno Pecho</td>
                                <td>94</td>
                                <td>98</td>
                                <td>102</td>
                                <td>106</td>
                                <td>110</td>
                                <td>114</td>
                            </tr>
                            <tr>
                                <td>Contorno Cintura</td>
                                <td>86</td>
                                <td>90</td>
                                <td>94</td>
                                <td>98</td>
                                <td>102</td>
                                <td>106</td>
                            </tr>
                            <tr>
                                <td>Largo Manga</td>
                                <td>24</td>
                                <td>24</td>
                                <td>27</td>
                                <td>27</td>
                                <td>29</td>
                                <td>31</td>
                            </tr>
                            <tr>
                                <td>Largo</td>
                                <td>67</td>
                                <td>69</td>
                                <td>71</td>
                                <td>73</td>
                                <td>75</td>
                                <td>77</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="inputs">
                <h4>Elija la tabla de medidas que desea ver</h4>
                <input type="radio" name="medidas" value="pantalon" @click="chooseMedidas = 'pantalon'">
                <input type="radio" name="medidas" value="remeraO" @click="chooseMedidas = 'remeraO'">
                <input type="radio" name="medidas" value="remeraV" @click="chooseMedidas = 'remeraV'">
                <input type="radio" name="medidas" value="buzo" @click="chooseMedidas = 'buzo'">
                <input type="radio" name="medidas" value="camisa" @click="chooseMedidas ='camisa'">
            </div>
            <div class="comprar-producto">
                <button @click="agregarAlCarrito" :class="{success: success}">{{messageSuccess}}</button>
            </div>
            <div class="message">
                <div v-if="showMessage">Por favor seleccione un talle.</div>
            </div>
        </div>
    </div>
    
</template>
<script>
export default{
    props: ['id'], //recibir el parametro id como prop
    data(){
        return {
            product:{},
            count: 1,
            chooseMedidas: null,
            selectedTalle: null,
            cantidadDisponible: null,
            showMessage: false,
            messageSuccess: 'Agregar al carrito',
            success: false,
        }
    },
    methods:{
        agregarAlCarrito(){
            if(this.selectedTalle == null){
                this.showMessage = true
                return
            }else{
                this.showMessage = false;
            }

            const productoEnCarrito = {
                producto: this.product,
                talle: this.selectedTalle,
                cantidad: this.count
            }

            this.$store.commit('agregarAlCarrito', productoEnCarrito);

            setTimeout(() => {
                this.success = true;
                this.messageSuccess = 'Producto agregado!';

                setTimeout(() => {
                    this.success = false;
                    this.messageSuccess = 'Agregar al carrito';
                }, 2300);
            }, 500);
        },
        selectTalla(talle) {
            this.selectedTalle = talle;

            this.cantidadDisponible = this.product[talle];

            if (this.count > this.cantidadDisponible) {
            this.count = this.cantidadDisponible;
            }
        },
        decrementCantidad() {
            if (this.count > 1) {
            this.count--;
            }
        },
        incrementCantidad() {
            if (this.count < this.cantidadDisponible) {
            this.count++;
            }
        },
        stockColor(stock) {
            if (stock == 0) {
                return { color: 'red' };
            } else if (stock <= 5) {
                return { color: 'orange' }; 
            } else if (stock <= 10) {
                return { color: 'yellow' };
            } else {
                return { color: 'green' };
            }
        },
        getStockStatus(stock) {
            if (stock == 0) {
                return 'Sin Stock';
            } else if (stock <= 5) {
                return 'Stock Bajo';
            } else if (stock == 10) {
                return 'Stock Medio';
            } else {
                return 'Stock Alto';
            }
        },
        loadProductDetails(){
            const productId = this.id;
            
            fetch('http://127.0.0.1:5000/productos/' + productId)
            .then(res => {
                if(res.ok){
                    return res.json()
                }
                else{
                    throw new Error ('Error al obtener el producto')
                }
            })
            .then(data => {
                this.product = data;
            })
            .catch(err => {
                console.error('Error: ', err)
            })
        },
    },
    mounted(){
        this.loadProductDetails();
    },
};
</script>

<style scoped>
.wrapper-producto{
    width: 70%;
    height: 100%;
    margin: 5% auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    justify-content: center;
    align-items: center;
}
.image-producto{
    width: 100%;
    backdrop-filter: blur(25px);
    box-shadow: 0px 20px 50px rgba(0,0,0,0.5);
    border-top: 1px solid rgba(255,255,255,0.3);
    border-left: 1px solid rgba(255,255,255,0.1);
    border-radius: 3px;
    padding: 30px 0;
}
.primary{
    width: 70%;
    height: 20%;
    margin: auto;
    overflow: hidden;
}
.primary img{
    width: 100%;
    border-bottom: 2px solid #27374D;
    padding-bottom: 30px;
    border-radius: 2px;
    object-fit: cover;
}


.datos-producto{
    width: 70%;
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: center;
    color: #27374D;
    margin: auto;
}
.nombre-producto{
    font-size: 1.5em;
    letter-spacing: 3px;
    border-bottom: 2px solid #27374D;
}
.valor-producto{
    font-size: 1.2em;
    margin: 25px 0;
    letter-spacing: 2px;
}
.cantidad-producto{
    width: 100px;
    height: 25px;
    border: 2px solid #27374D;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-radius: 2px;
}
.cantidad-producto span{
    font-size: 1.2em;
    width: 100%;
    text-align: center;
    transition: .5s;
}
.cantidad-producto span:nth-child(2){
    border-left: 1px solid #27374D;
    border-right: 1px solid #27374D;
}
.cantidad-producto span:not(:nth-child(2)):hover{
    color: #fff;
    background-color: #27374D;
    cursor: pointer;
}
.info-producto{
    letter-spacing: 2px;
    padding: 25px 0;
}

.info-talle{
    margin-bottom: 20px;
}
.span-talle{
    padding: 10px 0;
}
.span-talle span{
    padding: 5px;
    border: 2px solid #27374D;
    margin: 5px;
    cursor: not-allowed;
    text-align: center;
    transition: .5s ease;
    border-radius: 2px;
    background-color: rgb(231, 231, 231);
    color: #b8b8b8;
}


.span-talle span.available{
    background-color: transparent;
    color: #27374D;
    cursor: pointer;
}
.span-talle span.available:hover{
    color: white;
    background-color: #27374D;
}

.span-talle span.selected{
    color: white;
    background-color: #27374D;
}

.medidas{
    margin-top: 20px;
    letter-spacing: 1px;
    display: flex;
    width: 500px;
    overflow: hidden;
}
.medidas h3:nth-child(1){
    border-bottom: 1px solid #27374D;
    margin-bottom: 5px;
}
.comprar-producto{
    width: 100%;
}
.comprar-producto button{
    width: 100%;
    height: 35px;
    margin-top: 50px;
    cursor: pointer;
    background-color: #27374D;
    color: #fff;
    border: none;
    border-radius: 3px;
    letter-spacing: 2px;
    font-size: .9em;
    transition: .5s ease;
}
.comprar-producto button.success{
    background-color: green;
}

table{
    width: 500px;
    margin-right: 1px;
}
table,
table tr{
    border: 2px solid #27374D;
}
table td{
    border: 1px solid #27374D;
    padding: 3px;
    text-align: center;
}

.inputs{
    accent-color: #27374D;
    margin-top: 20px;
    padding: 5px 10px;
}
.inputs input{
    margin: 0 5px;
}

.message{
    color: red;
    margin-top: 5px;
    font-weight: 400;
}

@media (max-width: 768px){
    .wrapper-producto{
        height: 100%;
        width: 100%;
        margin: 15% auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-content: center;
    }
    .primary{
        width: 90%;
    }
    .primary img{
        height: 400px;
        /* object-fit: contain; */
    }
    .datos-producto{
        width: 90%;
        margin-top: 15%;
    }
    .valor-producto{
        font-size: 1.3em;
    }
    .cantidad-producto{
        width: 70%;
        height: 35px;
        align-items: center;
    }
    .cantidad-producto span{
        font-size: 1.6em;
        height: 100%;
    }
    .info-producto{
        font-size: 1.3em;
    }
    .info-talle h3{
        font-size: 1.4em;
    }
    .span-talle{
        margin-top: 5%;
    }
    .span-talle span{
        padding: 8px;
        font-size: 1.5em;
    }
    .title-medidas{
        font-size: 1.2em;
        margin-top: 10%;
    }
    .medidas{
        max-width: 340px;
        overflow: auto;
    }
    .comprar-producto button{
        margin-top: 5%;
        font-size: 1.1em;
    }
    .inputs h4{
        font-size: 1.2em;
        text-align: justify;
    }
    .inputs input{
        margin: 5% 20px;
        height: 20px;
        width: 20px;
    }
    .message{
        font-size: 1.2em;
        font-weight: 600;
    }
}

@media (min-width: 769px) and (max-width: 1200px){
    .wrapper-producto{
        width: 90%;
        height: 100%;
        margin: 12% auto;
        grid-template-columns: 40% 60%;
    }
    .primary{
        width: 90%;
        height: 100%;
    }
    .primary img{
        object-fit: contain;
    }
    .datos-producto{
        width: 90%;
    }
    .valor-producto{
        font-size: 1.6em;
    }
    .cantidad-producto{
        width: 200px;
        height: 30px;
    }
    .cantidad-producto span{
        font-size: 1.4em;
    }
    .info-producto{
        font-size: 1.1em;
    }
    .info-talle h3{
        font-size: 1.4em;
    }
    .span-talle{
        margin: 5% 0;
    }
    .span-talle span{
        margin: 4%;
        padding: 8px;
        font-size: 1.5em;
    }
    .comprar-producto button{
        font-size: 1.1em;
    }
    .title-medidas{
        font-size: 1.1em;
    }
    .medidas{
        max-width: 400px;
        overflow: auto;
    }
    .inputs h4{
        font-size: 1.1em;
    }
    .inputs input{
        margin: 5% 20px 0 20px;
        height: 20px;
        width: 20px;
    }
    .message{
        font-size: 1.1em;
        font-weight: 600;
    }
}
</style>