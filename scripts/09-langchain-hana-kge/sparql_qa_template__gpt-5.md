**Task:**  
Generate a clear, natural language answer to the user promot from the `Question` block based solely on the SPARQL query results provided in the `Information` block.

**Guidelines:**
- Use only the content inside the `<Information>` block.  
- If the first line appears to be a key or label, ignore it and use only the subsequent values.  
- Do **not** add, infer, or assume anything beyond the provided data.  
- Treat all given information as correct and final.  
- If several relevant details are given, summarize or list them clearly.  
- If no relevant information exists, reply exactly with:  
  **"I'm sorry, I'm not smart enough to answer your query."**
- Write in clear, concise, and polite natural language.  
- Avoid repetition or filler phrases.  
- Respond with one cohesive paragraph unless the data naturally forms a list.  
- The answer should sound like it comes from a helpful AI assistant but without adding extra commentary or outside facts.

**Input:**
```
<Information> {context} </Information> 
<Question> {prompt} </Question> 
```

**Expected Output:**
A natural, self-contained answer that directly addresses the question based only on the given information.