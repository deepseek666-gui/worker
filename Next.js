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
