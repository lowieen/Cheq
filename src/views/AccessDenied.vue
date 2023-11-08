<template>
    <div class="wrapper">
        <div class="container">
            <h2>Acceso Denegado!</h2>
            <p>Tu usuario no está permitido para ingresar en la administración de la pagina.</p>
        </div>
    </div>
</template>

<style scoped>
.wrapper{
    width: 100%;
    height: 100%;
}
.container{
    width: 80%;
    height: 75vh;
    margin: 2% auto;
    border-top: 2px solid #fff;
    border-radius: 3px;
    box-shadow: 0 5px 10px black;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color:  rgba(34,34,34,1);
}
h2{
    font-size: 3em;
    margin-bottom: 2%;
    color: #fff;
}
p{
    font-size: 1.5em;
    color: #acacac;
}
</style>