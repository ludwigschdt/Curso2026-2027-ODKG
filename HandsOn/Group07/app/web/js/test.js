import { select } from "./sparql.js";

const QUERY = `select (COUNT(?trainstop) AS ?count) where {
    ?trainstop a ns1:TrainStop .
}`;

const response = await select(QUERY);
document.getElementById("number").textContent = response.rows[0].count;
