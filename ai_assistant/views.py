from django.shortcuts import render

def ai_chat(request):

    answer = ""

    if request.method == "POST":

        question = request.POST.get("question", "").lower().strip()

        if "hello" in question or "hi" in question or "hey" in question:

            answer = """
👋 Hello!

Welcome to Organic Fresh Market AI Assistant.

I can help you choose healthy fruits and vegetables.

Try asking:
• Fruits rich in Vitamin C
• Vegetables for diabetes
• Foods for weight loss
• Iron-rich vegetables
"""

        elif "vitamin c" in question:

            answer = """
🍊 Fruits Rich in Vitamin C

✅ Orange
✅ Lemon
✅ Guava
✅ Kiwi
✅ Strawberry

Benefits:
• Boosts immunity
• Healthy skin
• Helps wound healing
• Rich in antioxidants
"""

        elif "diabetes" in question:

            answer = """
🥬 Best Vegetables for Diabetes

✅ Bitter Gourd
✅ Spinach
✅ Broccoli
✅ Cucumber
✅ Bottle Gourd

Benefits:
• Low Glycemic Index
• Rich in Fiber
• Helps control blood sugar
"""

        elif "weight" in question or "weight loss" in question:

            answer = """
🥗 Best Foods for Weight Loss

🍎 Apple
🥒 Cucumber
🍉 Watermelon
🥕 Carrot
🥬 Lettuce

Benefits:
• Low Calories
• High Fiber
• Keeps you full longer
"""

        elif "iron" in question:

            answer = """
🥬 Iron Rich Foods

✅ Spinach
✅ Beetroot
✅ Broccoli
✅ Drumstick Leaves

Benefits:
• Increases Hemoglobin
• Prevents Anemia
"""

        elif "protein" in question:

            answer = """
💪 Protein Rich Vegetables

✅ Green Peas
✅ Spinach
✅ Broccoli
✅ Corn
✅ Mushrooms

Benefits:
• Muscle Growth
• Better Energy
"""

        elif "heart" in question:

            answer = """
❤️ Foods for Heart Health

🥑 Avocado
🍅 Tomato
🥬 Spinach
🥦 Broccoli
🍎 Apple

Benefits:
• Reduces Cholesterol
• Good for Blood Pressure
"""

        elif "immunity" in question:

            answer = """
🛡️ Foods to Boost Immunity

🍊 Orange
🍋 Lemon
🧄 Garlic
🫚 Ginger
🌿 Turmeric

Benefits:
• Strong Immune System
• Helps Fight Infection
"""

        elif "children" in question or "kids" in question:

            answer = """
👶 Healthy Foods for Children

🍌 Banana
🍎 Apple
🥭 Mango
🥕 Carrot
🥔 Sweet Potato

Benefits:
• Growth
• Strong Bones
• Better Immunity
"""

        elif "pregnancy" in question or "pregnant" in question:

            answer = """
🤰 Healthy Foods During Pregnancy

🥬 Spinach
🍎 Apple
🍌 Banana
🥕 Carrot
🥛 Milk

Rich in Iron, Calcium and Vitamins.
"""

        elif "skin" in question:

            answer = """
✨ Foods for Healthy Skin

🥝 Kiwi
🍊 Orange
🥕 Carrot
🥑 Avocado
🍅 Tomato

Rich in Vitamins A, C and E.
"""

        elif "hair" in question:

            answer = """
💇 Foods for Healthy Hair

🥬 Spinach
🥚 Eggs
🥜 Nuts
🥕 Carrot
🥑 Avocado

Rich in Protein and Iron.
"""

        else:

            answer = """
🤖 Organic Fresh Market AI Assistant

Sorry, I couldn't understand your question.

You can ask:

🍊 Fruits rich in Vitamin C

🥬 Vegetables for Diabetes

💪 Protein-rich vegetables

❤️ Foods for Heart Health

🛡️ Foods for Immunity

⚖️ Foods for Weight Loss

👶 Healthy Foods for Children

🤰 Pregnancy Diet

✨ Foods for Healthy Skin

💇 Foods for Healthy Hair
"""

    return render(request, "ai/chat.html", {
        "answer": answer
    })
