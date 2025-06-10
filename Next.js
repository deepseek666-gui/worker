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
