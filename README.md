Que tal profe sabes que estoy en apuros, me desvie al principio del proyecto y
para no tener que hacer de nuevo la logica me enrosque a full con chat gpt 
intentando que mis formularios hereden directmanete los campos de los atributos de mis modelos
y asi no tener la necesidad de hacer una funcion distinta
para cada formulario, si no que una sola funcion resuelva los fomrularios dependiendo de la opcion elegida
en un formulario "padre" llamado producto, que resuelve primero dentro de ella misma, el cual contiene un choicefield
para cual cada choice que contiene, digamos cada opcion que yo le declare en el form, hace correspondencia dentro del mismo al respectivo
formulario que refiere al modelo que le corresponde. Logre que no se rompa el server ni nada
pero solo me aparece el formulario padre (producto), y no me resuelve posteriormente los formularios
respectivos a la clase de cada modelo.
 En sintesis, lo que quise hacer es que una sola funcion resuelva todos los forms dependiendo la opcion elegida 
dentro del primer form que haria referencia al modelo y mediante if y elif darle las tres posibilidades de formularios
a resolver dependiendo el modelo que la opcion del choicefield haga referencia.
