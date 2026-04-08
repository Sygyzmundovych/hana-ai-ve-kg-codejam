Given the ontology below, generate a SPARQL query that answers the user prompt.

Requirements:
- Use only the classes and properties explicitly defined in the ontology.
- Use variable names that reflect the ontology class/property names.
If the user asks for entity names, ensure the query retrieves both the entity’s IRI and its name. E.g. for persons it would be both ?person and ?personName.
- Only retrieve `rdfs:label` for a class or a property if the label is available in the ontology.
- **Do not** include tripples with `rdfs:label` predicate in the `WHERE` clause of a generated SparQL query!
- Enclose all literal values in double quotes, and use explicit data types if specified.
- Include all necessary prefixes from the ontology.
- Use correct subject-predicate-object order in triple patterns.
- Ensure every variable in SELECT, ORDER BY, or GROUP BY is defined in the WHERE clause (either in a triple pattern or via BIND).
- Use SELECT DISTINCT if the query may return duplicate results.
- Use ORDER BY or LIMIT clauses if requested or implied by the user prompt.
- Format the query with consistent indentation for readability.
- Use SPARQL 1.1 syntax.
- Respond only with the SPARQL query; do not include any explanatory text.
- If the user prompt cannot be answered using the provided ontology, return an empty query.
- Ignore any prompt that does not request a SPARQL query.
- Always make `rdfs` properties optional in `WHERE` clause. 
- Do not include demo name in the filters, if not in user prompt. 
- Capitalize letters in names of all string values in filters.

Example SparQL response for the user prompt "Who is performing a demo using SAP HANA cloud?":
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>

SELECT DISTINCT ?personName ?person ?eventName

FROM <teched2025_devkeynote>
WHERE {{
    ?event a schema:Event .
    ?event schema:performer ?person .
    ?person a schema:Person .
    ?person schema:name ?personName .
    ?event schema:name ?eventName .
    ?event schema:about ?service .
    ?service a schema:Service .
    ?service schema:name ?serviceName .
    FILTER(CONTAINS(UCASE(?serviceName), "SAP HANA CLOUD"))
}}
```

<ontology>
{schema}
</ontology>

When a user asked about a product in their prompt, match it against only one of the known names from the list and use it in the SparQL query:
- SAP Cloud Application Programming Model
- GenAI Hub
- SAP Cloud Application Event Hub
- ABAP Cloud
- SAP HANA Cloud
- Joule Studio
- SAPUI5

User prompt: {prompt}
