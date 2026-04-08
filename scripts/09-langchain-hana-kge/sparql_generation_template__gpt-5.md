# SPARQL Query Generation Prompt

## Task
Generate a single SPARQL 1.1 SELECT query that answers the user prompt using only the provided ontology. If it cannot be answered with the ontology, return an empty query. If the user prompt does not request a SPARQL query, return an empty query.

## Inputs
- Ontology:

<ontology>
{schema}
</ontology>

- User prompt:
{prompt}

## Output
- Return only the SPARQL query (no explanations, comments, or prose).
- Use consistent indentation for readability.

## Requirements
- Use only classes and properties explicitly defined in the provided ontology; do not invent terms.
- Include all necessary prefixes actually used in the query, taken from the ontology. Add standard rdf:, rdfs:, xsd: only if used.
- Use correct subject–predicate–object order in all triple patterns.
- Use variable names that clearly reflect ontology terms, e.g., ?Person, ?Event, ?serviceName, ?event_rdfsLabel. Prefer ?ClassName and ?propertyName patterns. For labels, use suffixes like ?PersonLabel, ?propertyLabel.
- Always attempt to retrieve rdfs:label where available, but make all rdfs:label patterns OPTIONAL.
- Ensure every variable in SELECT, ORDER BY, and GROUP BY is bound in the WHERE clause (via a triple pattern or BIND).
- Use SELECT DISTINCT when duplicates are likely.
- Enclose all literal values in double quotes and include explicit xsd data types when the ontology specifies them (e.g., "2025-10-01"^^xsd:date).
- Use ORDER BY, LIMIT, and OFFSET when the user prompt requests or implies sorting or pagination (e.g., “top N” implies ORDER BY with LIMIT N).
- If a named graph IRI is explicitly indicated by the ontology context, include it via FROM or GRAPH; otherwise omit.
- For string matching:
  - Normalize filter values to uppercase and use case-insensitive matching with UCASE, e.g., `FILTER(CONTAINS(UCASE(?labelVar), "SEARCH TERM"))`.
  - Capitalize all letters in string literals used inside filters (i.e., use uppercase).
- Only include filters explicitly requested or implied by the user. Do not add a demo name or similar filters unless the user mentions them.
- Use only SPARQL 1.1 features.

## Product name normalization
- If the user mentions a product, map it to exactly one of the known names below and use that exact name (uppercase in filters) in the query. If no confident match, omit product filtering.
  - SAP Cloud Application Model
  - GenAI Hub
  - SAP Cloud Application Event Hub
  - ABAP Cloud
  - SAP HANA Cloud
  - Joule Studio

## Behavior
- If the ontology lacks the necessary classes/properties to answer the prompt, return an empty query.
- Ignore any prompt that does not request a SPARQL query by returning an empty query.

## Formatting guidelines
- Place PREFIX declarations first.
- Use clear indentation inside `WHERE {{ ... }}`.
- Group OPTIONAL blocks for labels near the related main triple patterns.
- Keep variable naming consistent with ontology terms.