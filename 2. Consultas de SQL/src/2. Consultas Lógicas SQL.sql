-- Consultas lógicas SQL -> Daniel Recio

-- 1 Crea el esquema de la BBDD
-- 2 Muestra los nombres de todas las películas con una clasificación por edades de ‘Rʼ.
select "rating" as r_rating
from "film"
where "rating" = 'R';

-- 3 Encuentra los nombres de los actores que tengan un “actor_idˮ entre 30 y 40.
select concat("first_name",' ', "last_name") as actor_name
from "actor"
where "actor_id" between 30 and 40;

-- 4 Obtén las películas cuyo idioma coincide con el idioma original.
select "title" as same_film_language
from "film"
where "language_id" = "original_language_id";

-- 5 Ordena las películas por duración de forma ascendente.
select "title", "length" as film_duration
from "film"
order by "length" asc;

-- 6 Encuentra el nombre y apellido de los actores que tengan ‘Allenʼ en su apellido.
select concat("first_name", ' ', "last_name") as allen_surname
from "actor"
where "last_name" LIKE '%ALLEN%';

-- 7 Encuentra la cantidad total de películas en cada clasificación de la tabla “filmˮ y muestra la clasificación junto con el recuento.
select  "rating" , count(*) as film_rating
from "film"
group by rating;

-- 8 Encuentra el título de todas las películas que son ‘PG-13ʼ o tienen una duración mayor a 3 horas en la tabla film.
select "title" as pg13_or_3duration_films, 
       "length" as film_duration
from "film"
where "title" = 'PG-13' or "length" > 180;

-- 9 Encuentra la variabilidad de lo que costaría reemplazar las películas.
select variance("replacement_cost") as variance_replacement,
       stddev("replacement_cost") as stddev_replacement
from "film";

-- 10 Encuentra la mayor y menor duración de una película de nuestra BBDD.
select max("length") as max_film_duration, 
       min("length") as min_film_duration
from "film";

-- 11 Encuentra lo que costó el antepenúltimo alquiler ordenado por día.
select "amount" as antepenultimate_rental_amount
from "rental"
inner join "payment" on rental.rental_id = payment.rental_id
order by rental_date desc
limit 1
offset 2;

-- 12 Encuentra el título de las películas en la tabla “filmˮ que no sean ni ‘NC-17ʼ ni ‘Gʼ en cuanto a su clasificación.
select "title" as film_not_in_nc17_and_g
from "film"
where "rating" not in ('NC-17', 'G');

-- 13 Encuentra el promedio de duración de las películas para cada clasificación de la tabla film y muestra la clasificación junto con el promedio de duración.
select "rating", avg("length") as avg_duration
from "film"
group by "rating";

-- 14 Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.
select "title" as film_more_180min_duration
from "film"
where "length" > 180;

-- 15 ¿Cuánto dinero ha generado en total la empresa?
select sum("amount") as total_amount
from "payment";

-- 16 Muestra los 10 clientes con mayor valor de id.
select "customer_id" as most_customer_value_id
from "customer"
order by customer_id desc 
limit 10;

-- 17 Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igbyʼ.
select concat("first_name", ' ', "last_name") as actors_in_egg_igby_film
from "actor"
inner join "film_actor" on actor.actor_id = film_actor.actor_id
inner join "film" on film_actor.film_id = film.film_id
where film.title = 'EGG IGBY';

-- 18 Selecciona todos los nombres de las películas únicos.
select distinct "title" as distinct_title
from "film";

-- 19 Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla “filmˮ.
select "title" as comedy_and_more_180min_films
from "film"
inner join "film_category" on film.film_id = film_category.film_id
inner join "category" on film_category.category_id = category.category_id
where "name" = 'Comedy' and "length" > 180;

-- 20 Encuentra las categorías de películas que tienen un promedio de duración superior a 110 minutos y muestra el nombre de la categoría junto con el promedio de duración.
select "category"."name" as name_category,
       avg("film"."length") as average_length
from "film"
inner join "film_category" on film_category.film_id = film.film_id
inner join "category" on film_category.category_id = category.category_id
group by "category"."name" 
having avg("film"."length") > 110;

-- 21 ¿Cuál es la media de duración del alquiler de las películas?
select avg("rental_date" - return_date) as average_rental
from "rental"

-- 22 Crea una columna con el nombre y apellidos de todos los actores y actrices.
select concat("first_name", ' ', "last_name") as actor_actress_name
from "actor";

-- 23 Números de alquiler por día, ordenados por cantidad de alquiler de forma descendente.
select "rental_date", 
       count(rental_id) as rental_day_by_day
from "rental"
group by "rental_date"
order by rental_day_by_day desc;

-- 24 Encuentra las películas con una duración superior al promedio.
select "title" as film_more_average_length
from "film"
where "length" > (
select avg("length")
from "film");

-- 25 Averigua el número de alquileres registrados por mes.
select date_trunc('month', "rental_date") as "month", 
       count(*) as rents_per_month
from "rental"
group by "month"
order by "month";

-- 26 Encuentra el promedio, la desviación estándar y varianza del total pagado.
select avg("amount") as total_avg,
       variance("amount") as variance,
       stddev("amount") as stddev
from "payment"

-- 27 ¿Qué películas se alquilan por encima del precio medio?
select amount as average_film_price
from "payment"
where "amount" > (
select avg("amount")
from "payment");

-- 28 Muestra el id de los actores que hayan participado en más de 40 películas.
select "actor"."actor_id" as actor_id_more_than_40films
from "actor"
inner join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
group by "actor"."actor_id"
having count("film_actor"."film_id") > 40;

-- 29 Obtener todas las películas y, si están disponibles en el inventario, mostrar la cantidad disponible.
select "film"."film_id", "film"."title", count("inventory"."film_id") as availability_amount
from "film"
left join "inventory" on "film"."film_id" = "inventory"."film_id"
group by "film"."film_id";

-- 30 Obtener los actores y el número de películas en las que ha actuado.
select concat("first_name", ' ', "last_name") as actor_name,
       count("film_actor"."film_id") as number_of_films
from "actor"
left join "film_actor" on actor.actor_id = film_actor.actor_id
group by "actor"."actor_id";

-- 31 Obtener todas las películas y mostrar los actores que han actuado en ellas, incluso si algunas películas no tienen actores asociados.
select "film"."film_id", "film"."title", 
       "actor"."actor_id" as actor_id,
       concat("actor"."first_name", ' ', "actor"."last_name") as actor_name
from "film"
left join "film_actor" on "film"."film_id" = "film_actor"."film_id"
left join "actor" on "film_actor"."actor_id" = "actor"."actor_id";

-- 32 Obtener todos los actores y mostrar las películas en las que han actuado, incluso si algunos actores no han actuado en ninguna película.
select "actor"."actor_id",
       concat("first_name", ' ', "last_name") as actor_name,
       "film"."film_id", 
       "film"."title"
from "actor"
left join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
left join "film" on "film_actor"."film_id" = "film"."film_id";

-- 33 Obtener todas las películas que tenemos y todos los registros de alquiler.
select "title", "rental_rate"
from "film";

-- 34 Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.
select concat("first_name", ' ', "last_name") as customer_name,
       sum("payment"."amount") as total_amount
from "customer"
inner join "payment" on "customer"."customer_id" = "payment"."customer_id"
group by "customer_name"
order by "total_amount" desc
limit 5;

-- 35 Selecciona todos los actores cuyo primer nombre es 'Johnny'.
select "first_name" as johnny_name
from "actor"
where "first_name" = 'JOHNNY';

-- 36 Renombra la columna “first_nameˮ como Nombre y “last_nameˮ como Apellido.
select "first_name" as Nombre,
       "last_name" as Apellido
from "actor";

-- 37 Encuentra el ID del actor más bajo y más alto en la tabla actor.
select min("actor_id") as lowest_id,
       max("actor_id") as highest_id
from "actor";

-- 38 Cuenta cuántos actores hay en la tabla “actorˮ.
select count(*) as total_actors
from "actor";

-- 39 Selecciona todos los actores y ordénalos por apellido en orden ascendente.
select "first_name" as name,
       "last_name" as apellido
from "actor"
order by apellido asc;

-- 40 Selecciona las primeras 5 películas de la tabla “filmˮ.
select "title" as first_five_films
from "film"
order by title asc 
limit 5;

-- 41 Agrupa los actores por su nombre y cuenta cuántos actores tienen el mismo nombre. ¿Cuál es el nombre más repetido?
select "first_name", count(*) as repeated_names
from "actor"
group by "first_name"
order by repeated_names;

select "first_name", count(*) as repeated_names
from "actor"
group by "first_name"
order by repeated_names desc
limit 1;

-- 42 Encuentra todos los alquileres y los nombres de los clientes que los realizaron.
select concat("customer"."first_name", ' ', "customer"."last_name") as customer_name,
       "rental"."rental_id", 
       "rental"."rental_date"
from "rental"
inner join "customer" on "rental"."customer_id" = "customer"."customer_id";

-- 43 Muestra todos los clientes y sus alquileres si existen, incluyendo aquellos que no tienen alquileres.
select concat("customer"."first_name", ' ', "customer"."last_name") as customer_name,
       "rental"."rental_id", 
       "rental"."rental_date"
from "customer"
left join "rental" on "customer"."customer_id" = "rental"."customer_id";

-- 44 Realiza un CROSS JOIN entre las tablas film y category. ¿Aporta valor esta consulta? ¿Por qué? Deja después de la consulta la contestación.
select "film"."film_id", "film"."title", 
       "category"."category_id", "category"."name"
from "film"
cross join "category";

/* Esta consulta no aporta valor, porque entre las dos tablas no existe una columna coincidente,
por lo tanto, los valores no tienen una cohesión entre ellos. */

-- 45 Encuentra los actores que han participado en películas de la categoría 'Action'.
select concat("first_name", ' ', "last_name") as actor_name
from "actor"
inner join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
inner join "film_category" on "film_actor"."film_id" = "film_category"."film_id"
inner join "category" on "film_category"."category_id" = "category"."category_id"
where "category"."name" = 'Action';

-- 46 Encuentra todos los actores que no han participado en películas.
select concat("first_name", ' ', "last_name") as actor_name
from "actor"
left join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
where "film_actor"."actor_id" is null;

-- 47 Selecciona el nombre de los actores y la cantidad de películas en las que han participado.
select concat("first_name", ' ', "last_name") as actor_name,
       count("film_actor"."film_id") as number_of_films
from "actor"
left join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
group by actor_name;

-- 48 Crea una vista llamada “actor_num_peliculasˮ que muestre los nombres de los actores y el número de películas en las que han participado.
create view "actor_num_peliculas"
select concat("first_name", ' ', "last_name", ' ', count("film_actor"."film_id")) as actor_num_films
from "actor"
left join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
group by "actor"."first_name", "actor"."last_name";

-- 49 Calcula el número total de alquileres realizados por cada cliente.
select concat("first_name", ' ', "last_name") as actor_name,
       count("rental"."rental_id") as customer_rental_num
from "customer"
inner join "rental" on "customer"."customer_id" = "rental"."customer_id"
group by "customer"."first_name", "customer"."last_name";

-- 50 Calcula la duración total de las películas en la categoría 'Action'.
select sum("film"."length") as action_film_length
from "film"
inner join "film_category" on "film"."film_id" = "film_category"."film_id"
inner join "category" on "film_category"."category_id" = "category"."category_id"
where "category"."name" = 'Action';
.
-- 51 Crea una tabla temporal llamada “cliente_rentas_temporalˮ para almacenar el total de alquileres por cliente.
create temporary table "cliente_rentas_temporal" as
select concat("first_name", ' ', "last_name", ' ', 
       count("rental"."rental_id")) as customer_rental_num
from "customer"
inner join "rental" on "customer"."customer_id" = "rental"."customer_id"
group by "customer"."first_name", "customer"."last_name";

-- 52 Crea una tabla temporal llamada “peliculas_alquiladasˮ que almacene las películas que han sido alquiladas al menos 10 veces.
create temporary table "peliculas_alquiladas" as
select "film"."film_id", "film"."title", count("rental"."rental_id")
from "film"
inner join "inventory" on "film"."film_id" = "inventory"."film_id"
inner join "rental" on "inventory"."inventory_id" = "rental"."rental_id"
group by "film"."film_id", "film"."title"
having count("rental"."rental_id") >= 10;

-- 53 Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre ‘Tammy Sandersʼ y que aún no se han devuelto. Ordena los resultados alfabéticamente por título de película.
select "film"."title" as film_title
from "customer" 
inner join "rental" on "customer"."customer_id" = "rental"."customer_id"
inner join "inventory" on "rental"."inventory_id" = "inventory"."inventory_id"
inner join "film" on "inventory"."film_id" = "film"."film_id"
where "customer"."first_name" = 'TAMMY' 
      and "customer"."last_name" = 'SANDERS'
      and "rental"."return_date" is null
order by film_title;

-- 54 Encuentra los nombres de los actores que han actuado en al menos una película que pertenece a la categoría ‘Sci-Fiʼ. Ordena los resultados alfabéticamente por apellido.
select concat("actor"."first_name", ' ', "actor"."last_name") as actor_name
from "actor"
inner join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
inner join "film" on "film_actor"."film_id" = "film"."film_id"
inner join "film_category" on "film"."film_id" = "film_category"."film_id"
inner join "category" on "film_category"."category_id" = "category"."category_id"
where "category"."name" = 'Sci-Fi'
order by actor_name;

-- 55 Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron después de que la película ‘Spartacus Cheaperʼ se alquilara por primera vez. Ordena los resultados alfabéticamente por apellido.
select concat("actor"."first_name", 
       "actor"."last_name") as actor_name
from "actor" 
inner join "film_actor" on "actor"."actor_id" = "film_actor"."actor_id"
inner join "film" on "film_actor"."film_id" = "film"."film_id"
inner join "inventory" on "film"."film_id" = "inventory"."film_id"
inner join "rental" on "inventory"."inventory_id" = "rental"."inventory_id"
where "rental"."rental_date" > (
      select min("rental"."rental_date")
      from"film"
      inner join "inventory" on "film"."film_id" = "inventory"."film_id"
      inner join "rental" on "inventory"."inventory_id" = "rental"."inventory_id"
      where "film"."title" = 'SPARTACUS CHEAPER')
group by actor_name
order by actor_name;

-- 56 Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría ‘Musicʼ.
select concat("first_name", ' ', "last_name") as actor_name
from "actor"
where "actor"."actor_id" not in (
      select "film_actor"."actor_id"
      from "film_actor"
      inner join "film" on "film_actor"."film_id" = "film"."film_id"
      inner join "film_category" on "film"."film_id" = "film_category"."film_id"
      inner join "category" on "film_category"."category_id" = "category"."category_id"
      where "category"."name" = 'Music')
order by "actor_name";

-- 57 Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.
select "film"."film_id", "film"."title", count("rental"."rental_date") 
from "film"
inner join "inventory" on "film"."film_id" = "inventory"."film_id"
inner join "rental" on "inventory"."inventory_id" = "rental"."rental_id"
group by "film"."film_id"
having count("rental"."rental_date") > 8;

-- 58 Encuentra el título de todas las películas que son de la misma categoría que ‘Animationʼ.
select "film"."title" as film_title
from "film"
inner join "film_category" on "film"."film_id" = "film_category"."film_id"
inner join "category" on "film_category"."category_id" = "category"."category_id"
where "category"."name" = 'Animation';

-- 59 Encuentra los nombres de las películas que tienen la misma duración que la película con el título ‘Dancing Feverʼ. Ordena los resultados alfabéticamente por título de película.
select "film"."title" as film_title
from "film" 
where "film"."length" = (
      select "film"."length"
      from "film" 
      where "film"."title" = 'DANCING FEVER')
order by "film_title";

-- 60 Encuentra los nombres de los clientes que han alquilado al menos 7 películas distintas. Ordena los resultados alfabéticamente por apellido.
select "customer"."first_name",
       "customer"."last_name" as apellido
from "customer"
inner join "rental" on "customer"."customer_id" = "rental"."customer_id"
inner join "inventory" on "rental"."inventory_id" = "inventory"."inventory_id"
inner join "film" on "inventory"."film_id" = "film"."film_id"
group by "customer"."first_name", "customer"."last_name"
having count(distinct "film"."film_id") >= 7
order by apellido;

-- 61 Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres.
select "category"."name" as category_name, 
       count("rental"."rental_id") as total_rentals
from "category" 
inner join "film_category" on "category"."category_id" = "film_category"."category_id" 
inner join "film" on "film_category"."film_id" = "film"."film_id"
inner join "inventory" on "film"."film_id" = "inventory"."film_id"
inner join "rental" on "inventory"."inventory_id" = "rental"."inventory_id" 
group by "category"."name"
order by "total_rentals" desc;

-- 62 Encuentra el número de películas por categoría estrenadas en 2006.
select "category"."name" as category_name,
       count("film"."film_id") as number_of_films
from "film"
inner join "film_category" on "film"."film_id" = "film_category"."film_id"
inner join "category" on "film_category"."category_id" = "category"."category_id"
where "film"."release_year" = 2006
group by "category"."name"
order by "category_name";

-- 63 Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.
select concat("first_name", ' ', "last_name") as staff_name,
       "staff"."store_id",
       "staff"."address_id",
       "store"."address_id",
       "store"."store_id"
from "staff"
cross join "store";

-- 64 Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas. 
select "customer"."customer_id", 
       concat("customer"."first_name", "customer"."last_name") as customer_name,
       count("rental"."rental_id") as "total_rentals"
from "customer"
left join "rental" on "customer"."customer_id" = "rental"."customer_id"
GROUP BY "customer"."customer_id"
ORDER BY "total_rentals" desc;