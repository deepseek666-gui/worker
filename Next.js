const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${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}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "openai/gpt-4o",  // or any supported model
    messages: chatHistory,
  }),
});
