# # # c = (29-32)*5//9
# # # print(c)    

# # def normalize(lst):
# #     min_val, max_val = min(lst), max(lst)
# #     return [(x - min_val) / (max_val - min_val) for x in lst]

# # lst = [10, 20, 30, 40, 50]
# # normalized_lst = normalize(lst)
# # print(normalized_lst)   

# import pandas as pd
# import numpy as np  
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.DataFrame({
#     'A': np.random.rand(10),
#     'B': np.random.rand(10),
#     'C': np.random.rand(10)
# })

# sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
# plt.show()

# n = int(input("Enter a number: ")   )
# def is_even(n):
#     if n % 2 == 0 :
#         return True
#     else:
#         return False

# print(is_even(n))   
# print(oct(23))

# li = [3,4,5,20,5,25,1,3]
# li.pop(1)
# print(li)

# x = 10
# lst = [x for x in range(5)]
# print(x)

# n = 16
# res = ("even","odd")
# print(res[n%2])
# import numpy as np
# e = np.array(1, ndmin=12)
# print(e)

""" Palindrome Check """
# n = 11123
# num = n
# result = 0
# while num > 0:
#     last_digit = num % 10
#     result = result * 10 + last_digit
#     num //= 10
# print(n == result)


""" armstrong number """
# n = 153  # You can change this value to test other numbers
# num = n
# order = len(str(n))
# result = 0

# while num > 0:
#     digit = num % 10
#     result += digit ** order
#     num //= 10

# print(f"{n} is an Armstrong number: {n == result}")


""" check the container have duplicate or not """
# nums = [1,2,3,43,2,1,3,2]
# def has_duplicates(nums):
#    seen = len(set(nums))
#    if len(nums) == seen:
#       return True
#    return False   

""" room and keys """

# rooms = [[1],[2],[3],[]]
# from typing import List
# # rooms = [[1,3],[3,0,1],[2],[0]]
# def canVisitAllRooms(rooms: List[List[int]]) -> bool:
#     visited = set()
#     def dfs(room):
#         visited.add(room)
#         for key in rooms[room]:
#             if key not in visited:
#                 dfs(key)
#     dfs(0)
#     return len(visited) == len(rooms)
# print(canVisitAllRooms(rooms))


""" kth largest number  """

# def find_kth_largest(nums, k):
#     if k < 1 or k > len(nums):
#         return None
#     nums.sort(reverse=True)
#     return nums[k - 1]
""" AI Agent """
# class AIAgent:
#     def __init__(self, name, skills):
#         self.name = name
#         self.skills = skills

#     def perform_task(self, task):
#         if task in self.skills:
#             return f"{self.name} is performing task: {task}"
#         else:
#             return f"{self.name} does not have the skill to perform task: {task}"

# # Example usage
# agent = AIAgent("Jarvis", ["speak", "listen", "search web", "control smart home"])
# print(agent.perform_task("speak"))
# print(agent.perform_task("cook dinner"))

class GeminiAIAgent:
    def __init__(self, name="Gemini", capabilities=None):
        self.name = name
        self.capabilities = capabilities if capabilities is not None else []
        print(f"{self.name} AI Agent initialized with capabilities: {', '.join(self.capabilities)}")

    def add_capability(self, capability):
        if capability not in self.capabilities:
            self.capabilities.append(capability)
            print(f"{self.name} now has the capability: {capability}")
        else:
            print(f"{self.name} already has the capability: {capability}")

    def remove_capability(self, capability):
        if capability in self.capabilities:
            self.capabilities.remove(capability)
            print(f"{self.name} no longer has the capability: {capability}")
        else:
            print(f"{self.name} does not have the capability: {capability}")

    def process_input(self, user_input):
        print(f"{self.name} received input: '{user_input}'")
        response = self._analyze_and_respond(user_input)
        return response

    def _analyze_and_respond(self, user_input):
        user_input_lower = user_input.lower()

        if "hello" in user_input_lower or "hi" in user_input_lower:
            return "Hello there! How can I assist you today?"
        elif "what can you do" in user_input_lower:
            if self.capabilities:
                return f"I can do many things, including: {', '.join(self.capabilities)}. What would you like me to do?"
            else:
                return "I am a general-purpose AI. I can process information and respond to your queries."
        elif "time" in user_input_lower:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        elif "date" in user_input_lower:
            return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."
        elif "search for" in user_input_lower:
            query = user_input_
            query = query.replace("search for", "").strip()
            if "web_search" in self.capabilities:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                return f"Searching the web for: {query}"
            else:
                return "I don't have the web search capability enabled."
        elif "open" in user_input_lower:
            app_name = user_input_lower.replace("open", "").strip()
            if "application_control" in self.capabilities:
                try:
                    if "browser" in app_name:
                        webbrowser.open("https://www.google.com")
                        return "Opening web browser."
                    elif "notepad" in app_name:
                        subprocess.Popen("notepad.exe")
                        return "Opening Notepad."
                    elif "calculator" in app_name:
                        subprocess.Popen("calc.exe")
                        return "Opening Calculator."
                    else:
                        return f"I can't open '{app_name}'. Please specify a known application."
                except Exception as e:
                    return f"Error opening application: {e}"
            else:
                return "I don't have the application control capability enabled."
        elif "tell me about" in user_input_lower:
            topic = user_input_lower.replace("tell me about", "").strip()
            if "knowledge_base" in self.capabilities:
                # This would be a more complex integration with a knowledge base or API
                return f"I'm looking up information about {topic}."
            else:
                return "I don't have a knowledge base to provide detailed information."
        elif "set a reminder" in user_input_lower:
            if "reminders" in self.capabilities:
                # This would require more sophisticated natural language processing
                return "I can set reminders, but I need more details about the time and message."
            else:
                return "I don't have the reminder capability enabled."
        elif "thank you" in user_input_lower or "thanks" in user_input_lower:
            return "You're welcome! Is there anything else I can help you with?"
        elif "goodbye" in user_:
            return "Goodbye! Have a great day."
        
print("Manav Singh")

a = 10 
b = 20
sum = a + b
print("sum =",sum)