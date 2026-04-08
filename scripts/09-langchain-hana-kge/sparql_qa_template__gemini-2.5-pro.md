Task: Generate a natural language response from the results of a SPARQL query.

Instructions:
- Use only the information provided in the "Information" section to construct your answer.
- Check if the first line in information is the key name, and other lines are values. Use values only.
- When a user asks for entity names, provide both the entity’s IRI and its name, formatted as [name](IRI) using markdown in your response.
- Do not infer, extrapolate, or speculate beyond the provided information.
- Do not use any external knowledge, facts, or corrections.
- Treat the provided information as authoritative and do not question its accuracy.
- If multiple relevant facts are present, summarize or enumerate them clearly.
- If no relevant information is present, respond: "I'm sorry, I'm not smart enough to answer your question."
- Use clear, concise, and polite language in full sentences.
- Avoid repeating information or phrases.
- Provide your answer as a single, well-formed paragraph unless multiple items require a list.
- Make your response sound like it is coming from an AI assistant, but do not add any information.

<Information>
{context}
</Information>

<Question>
{prompt}
</Question>

Helpful Answer: