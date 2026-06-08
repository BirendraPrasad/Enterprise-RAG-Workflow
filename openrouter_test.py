from app.llm import generate_answer

answer = generate_answer(
    "How do I charge Galaxy Watch 5 Pro?",
    "To charge Galaxy Watch 5 Pro, connect the magnetic charger to the back of the watch."
)

print(answer)