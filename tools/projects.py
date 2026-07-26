# -*- coding: utf-8 -*-
"""Content for the eight project guides."""

PROJECTS = [

# ───────────────────────────── 01 ─────────────────────────────
{
"num":"01","slug":"01-terminal-toolkit","title":"Terminal toolkit",
"weeks":"Weeks 1–2","commit":"init: first commits",
"summary":"Four small command-line tools. Everything you need to write a working program.",
"intro":"""
<p>The goal of these two weeks is not the tools. It's getting to the point where writing a small program stops feeling like magic and starts feeling like typing.</p>
<p>You'll build four things in one repository. Each is small enough to finish in a session or two, and each adds one new idea. Nothing here has a user interface, nothing looks good, and that's fine — you're learning to make a computer do what you say.</p>
""",
"sessions":[
 {"n":1,"title":"Printing, variables, and your first script",
  "teach":"""
<p>A Python program is a text file that runs top to bottom. Make a file called <code>hello.py</code>, put one line in it, and run it with <code>python3 hello.py</code>.</p>
<div class="code"><button class="copy">Copy</button><pre><code>print("Hello")</code></pre></div>
<p>A <strong>variable</strong> is a name for a value. The <code>=</code> sign means "put this value in this name" — it is not the maths equals.</p>
<div class="code"><button class="copy">Copy</button><pre><code>name = "Sam"
age = 34
print(name)</code></pre></div>
<p>To put a variable inside a sentence, use an <strong>f-string</strong> — an <code>f</code> before the quote, and curly braces around the variable:</p>
<div class="code"><button class="copy">Copy</button><pre><code>print(f"{name} is {age} years old")</code></pre></div>
<p><code>input()</code> asks the person running the program to type something. Whatever they type comes back as text.</p>
""",
  "build":"<p>Write a script that asks for someone's name and their favourite food, then prints a sentence using both. Commit it.</p>",
  "check":"You can create a file, run it from the terminal, store input in variables, and print a sentence built from them."},

 {"n":2,"title":"Numbers, and why input lies to you",
  "teach":"""
<p>Here is the first thing that will confuse you, and it confuses everyone. <code>input()</code> always gives you <strong>text</strong>, even when the person typed a number.</p>
<div class="code"><button class="copy">Copy</button><pre><code>age = input("Age: ")   <span class="c"># person types 34</span>
print(age + 1)         <span class="c"># TypeError!</span></code></pre></div>
<p>Python is telling you it can't add a number to a piece of text. You have to convert it first — <code>int()</code> for whole numbers, <code>float()</code> for decimals:</p>
<div class="code"><button class="copy">Copy</button><pre><code>age = int(input("Age: "))
print(age + 1)         <span class="c"># 35</span></code></pre></div>
<p>Maths works how you'd expect: <code>+ - * /</code>. Two extras worth knowing: <code>**</code> is "to the power of", and <code>round(x, 2)</code> rounds to two decimal places, which you'll want for anything involving money.</p>
""",
  "build":"<p>Build <code>converter.py</code>: ask for a temperature in Celsius, print it in Fahrenheit. Then add kilometres to miles. Round the answers sensibly.</p>",
  "check":"You understand why <code>int()</code> and <code>float()</code> exist and you can read a TypeError without panicking."},

 {"n":3,"title":"Making decisions",
  "teach":"""
<p><code>if</code> runs a block of code only when something is true. The indentation is not decoration — it's how Python knows what's inside the <code>if</code>.</p>
<div class="code"><button class="copy">Copy</button><pre><code>temperature = 31

if temperature > 30:
    print("Too hot")
elif temperature > 20:
    print("Nice")
else:
    print("Bring a coat")</code></pre></div>
<p>The comparisons: <code>&gt;</code> <code>&lt;</code> <code>&gt;=</code> <code>&lt;=</code> for size, <code>==</code> for "is the same as", <code>!=</code> for "is not the same as".</p>
<div class="note warn"><div class="lbl">The classic mistake</div><p>One <code>=</code> assigns a value. Two <code>==</code> asks a question. Using <code>=</code> where you meant <code>==</code> is something every programmer alive has done, usually more than once.</p></div>
<p>You can combine conditions with <code>and</code> and <code>or</code>, and flip one with <code>not</code>.</p>
""",
  "build":"<p>Start <code>guess.py</code>. Pick a secret number in the code, ask the person for a guess, and tell them whether they were too high, too low, or correct. One guess only for now.</p>",
  "check":"You can write a branching decision and you know the difference between <code>=</code> and <code>==</code>."},

 {"n":4,"title":"Loops, and repeating yourself properly",
  "teach":"""
<p>A <code>while</code> loop repeats as long as something stays true:</p>
<div class="code"><button class="copy">Copy</button><pre><code>count = 3
while count > 0:
    print(count)
    count = count - 1
print("Go")</code></pre></div>
<p>A <code>for</code> loop runs once for each item in a collection:</p>
<div class="code"><button class="copy">Copy</button><pre><code>for colour in ["red", "green", "blue"]:
    print(colour)

for n in range(5):      <span class="c"># 0, 1, 2, 3, 4</span>
    print(n)</code></pre></div>
<p><code>break</code> escapes a loop immediately. Use it when the person guesses correctly.</p>
<div class="note"><div class="lbl">If it never stops</div><p>Press <code>ctrl + c</code>. You've written a loop whose condition never becomes false — usually because you forgot to change the variable it's checking.</p></div>
<p>To pick a random number, use the <code>random</code> module, which comes with Python:</p>
<div class="code"><button class="copy">Copy</button><pre><code>import random
secret = random.randint(1, 100)</code></pre></div>
""",
  "build":"<p>Finish the guessing game: random secret number, keep asking until they get it, count the guesses and tell them at the end. Then build <code>dice.py</code> — roll any number of dice with any number of sides.</p>",
  "check":"You can write both kinds of loop and you know which to reach for."},

 {"n":5,"title":"Functions",
  "teach":"""
<p>A function is a named piece of code you can run whenever you like. It's how you stop repeating yourself and how programs stay readable past about fifty lines.</p>
<div class="code"><button class="copy">Copy</button><pre><code>def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

result = celsius_to_fahrenheit(20)
print(result)   <span class="c"># 68.0</span></code></pre></div>
<p><code>def</code> defines it, the name in brackets is the <strong>parameter</strong> — a value handed in when it's called — and <code>return</code> sends an answer back.</p>
<div class="note warn"><div class="lbl">print is not return</div><p>This trips up nearly everyone. <code>print</code> shows something on screen and gives back nothing. <code>return</code> hands a value back to whatever called the function, so it can be stored and used. A function that prints instead of returning is a function you can't build anything on top of.</p></div>
<p>Good functions do <strong>one thing</strong> and have a name that says what that thing is. If you can't name it clearly, it's probably doing too much.</p>
""",
  "build":"<p>Go back through all three tools and pull the logic into functions. Then build <code>tip.py</code>: take a bill total, a tip percentage and a number of people, and return what each person owes.</p>",
  "check":"You can write a function that returns a value, and you can explain why returning beats printing."},

 {"n":6,"title":"Tidy up and write it up",
  "teach":"""
<p>Two weeks in, go back over everything with fresh eyes.</p>
<p><strong>Handle bad input.</strong> What happens if someone types "banana" when you asked for a number? Right now, a crash. Wrap the risky conversion:</p>
<div class="code"><button class="copy">Copy</button><pre><code>try:
    age = int(input("Age: "))
except ValueError:
    print("That wasn't a number.")</code></pre></div>
<p><strong>Rename things.</strong> Any variable called <code>x</code>, <code>temp</code> or <code>data</code> should be renamed to say what it holds. This is the cheapest possible improvement to code quality.</p>
<p><strong>Write the README.</strong> Use the template in the reference section. Include the "what I learned" part properly — it's the bit that's actually worth something.</p>
""",
  "build":"<p>Every tool survives nonsense input. Every variable has a meaningful name. README written. Everything pushed.</p>",
  "check":"Someone else could clone your repo and run all four tools from your README alone."}
],
"traps":[
 ("Making it look nice","It's a terminal. Fancy formatting is procrastination dressed as work."),
 ("Copying without reading","If you paste something and it works but you can't explain it, you've learned nothing. Delete it and type it out."),
 ("Waiting to commit","Commit when it works, and when it half works. Fifteen small commits beats one big one.")
],
"stretch":[
 "Give the guessing game a difficulty setting that changes the range.",
 "Make the dice roller show each individual roll as well as the total.",
 "Add a loop to the converter so it keeps going until the person types 'quit'."
],
"done":"Four scripts run without crashing, each survives nonsense input, the README explains how to run each one, and there are 15+ commits."
},

# ───────────────────────────── 02 ─────────────────────────────
{
"num":"02","slug":"02-expense-tracker","title":"Expense tracker",
"weeks":"Weeks 3–4","commit":"feat: data that survives a restart",
"summary":"Your first program that remembers things. Lists, dictionaries, and files.",
"intro":"""
<p>This project has a trick built into it, and it's worth knowing about now so you recognise it when it happens.</p>
<p>You'll spend the first week building something that works nicely — add an expense, list them, total them up. Then you'll close it, reopen it, and everything will be gone. That moment is the entire point of the project. Everything you learn in week two exists to solve it.</p>
""",
"sessions":[
 {"n":1,"title":"Lists",
  "teach":"""
<p>A list holds several values in order. Square brackets, comma separated:</p>
<div class="code"><button class="copy">Copy</button><pre><code>shopping = ["milk", "bread", "eggs"]

print(shopping[0])        <span class="c"># milk — counting starts at 0</span>
print(len(shopping))      <span class="c"># 3</span>

shopping.append("cheese") <span class="c"># add to the end</span>
shopping.remove("bread")  <span class="c"># take one out</span>

for item in shopping:
    print(item)</code></pre></div>
<p>Counting from zero is standard across nearly every programming language. The first item is <code>[0]</code>, the last is <code>[-1]</code>. Asking for an index that doesn't exist gives you an <code>IndexError</code>.</p>
""",
  "build":"<p>A script that keeps a list of expense amounts. Add one, show them all, print the total using <code>sum()</code>.</p>",
  "check":"You can build a list, add to it, loop over it, and total it."},

 {"n":2,"title":"Dictionaries, and data with shape",
  "teach":"""
<p>A list of amounts isn't enough — an expense has a description, a category and a date too. A <strong>dictionary</strong> stores labelled values:</p>
<div class="code"><button class="copy">Copy</button><pre><code>expense = {
    "description": "Coffee",
    "amount": 3.40,
    "category": "food"
}

print(expense["amount"])       <span class="c"># 3.4</span>
expense["amount"] = 3.60       <span class="c"># change it</span></code></pre></div>
<p>The real shape you want is a <strong>list of dictionaries</strong> — several expenses, each with labelled fields:</p>
<div class="code"><button class="copy">Copy</button><pre><code>expenses = [
    {"description": "Coffee", "amount": 3.40, "category": "food"},
    {"description": "Bus",    "amount": 2.80, "category": "travel"},
]

for e in expenses:
    print(f"{e['description']}: £{e['amount']}")</code></pre></div>
<p>Asking for a key that isn't there gives a <code>KeyError</code>. Use <code>e.get("category", "unknown")</code> when a field might be missing.</p>
""",
  "build":"<p>Rework your tracker so each expense is a dictionary with description, amount and category. Print them as a neat table.</p>",
  "check":"You're comfortable with a list of dictionaries and can get at any field inside it."},

 {"n":3,"title":"A menu that keeps running",
  "teach":"""
<p>Real tools don't do one thing and exit. They show options and wait. That's a <code>while</code> loop with a menu inside:</p>
<div class="code"><button class="copy">Copy</button><pre><code>while True:
    print("1: add   2: list   3: quit")
    choice = input("> ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        break
    else:
        print("Didn't understand that.")</code></pre></div>
<p><code>while True</code> loops forever; <code>break</code> is the only way out. Notice the menu loop doesn't <em>do</em> anything itself — it decides which function to call. That's the structure to aim for.</p>
<div class="note"><div class="lbl">One function, one job</div><p>You want separate functions for adding, listing, deleting and totalling. If you end up with one function called <code>do_everything()</code>, you'll fight it for the rest of the project.</p></div>
""",
  "build":"<p>Menu loop with add, list, delete and total. Each one its own function.</p>",
  "check":"Your program runs until told to stop, and each menu option calls a separate, sensibly named function."},

 {"n":4,"title":"The crash — and files",
  "teach":"""
<p>Close your program. Open it again. Everything's gone.</p>
<p>Variables live in memory, and memory is wiped when the program ends. To keep anything you have to write it to a file on disk.</p>
<div class="code"><button class="copy">Copy</button><pre><code><span class="c"># writing</span>
with open("notes.txt", "w") as f:
    f.write("hello")

<span class="c"># reading</span>
with open("notes.txt", "r") as f:
    contents = f.read()</code></pre></div>
<p>The <code>with</code> block closes the file for you when it finishes, even if something goes wrong. Always use it.</p>
<p><code>"w"</code> means write — and it <strong>wipes the file first</strong>. <code>"r"</code> means read. <code>"a"</code> appends to the end.</p>
""",
  "build":"<p>Practice: save a list of names to a text file and read them back. Don't wire it into the tracker yet — text files are the wrong tool for structured data, and the next session explains why.</p>",
  "check":"You can write to a file and read it back, and you know <code>\"w\"</code> destroys what was there."},

 {"n":5,"title":"JSON — saving data that has shape",
  "teach":"""
<p>Your expenses are a list of dictionaries. Saving that as plain text means inventing a format and writing code to pick it apart again. <strong>JSON</strong> already solved this.</p>
<div class="code"><button class="copy">Copy</button><pre><code>import json

<span class="c"># save</span>
with open("expenses.json", "w") as f:
    json.dump(expenses, f, indent=2)

<span class="c"># load</span>
with open("expenses.json", "r") as f:
    expenses = json.load(f)</code></pre></div>
<p>That's it. Your list of dictionaries goes out and comes back with its structure intact. Open the file in VS Code and look at it — it's readable, which is part of why JSON won.</p>
<p>One problem: the very first time you run it there's no file yet, and <code>json.load</code> will crash. Handle it:</p>
<div class="code"><button class="copy">Copy</button><pre><code>def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []</code></pre></div>
<p>No file means no expenses yet, so return an empty list. That's not a workaround — it's the correct behaviour.</p>
""",
  "build":"<p>Wire it in. Load on start, save after every change. Close it, reopen it, and watch your data still be there.</p>",
  "check":"Your data survives a restart. This is the project's whole purpose."},

 {"n":6,"title":"Filtering, totals, and writing it up",
  "teach":"""
<p>Now the data persists, make it useful. Filtering a list by a condition:</p>
<div class="code"><button class="copy">Copy</button><pre><code>food = [e for e in expenses if e["category"] == "food"]</code></pre></div>
<p>That's a <strong>list comprehension</strong> — read it as "e for every e in expenses, where the category is food". It's the same as a <code>for</code> loop with an <code>if</code>, written on one line. Write it the long way first if that's clearer, then try shortening it.</p>
<p>Totalling one field across a list:</p>
<div class="code"><button class="copy">Copy</button><pre><code>total = sum(e["amount"] for e in expenses)</code></pre></div>
""",
  "build":"<p>Add: total by category, a filter by category, and a sort by amount. Then the README — include what happened when you first closed the program.</p>",
  "check":"You can filter and summarise a list of dictionaries, and your README tells the story of the project."}
],
"traps":[
 ("One giant function","If <code>add_expense()</code> is also saving the file and printing a summary, split it up. One job each."),
 ("Forgetting to save","Data changes in memory but never reaches disk. Save after every change that matters."),
 ("Floats and money","<code>0.1 + 0.2</code> doesn't give exactly <code>0.3</code> in any language. For this project just round when displaying. Real financial software stores pennies as whole numbers.")
],
"stretch":[
 "Add a date to each expense using the <code>datetime</code> module.",
 "Show a monthly total, grouped by month.",
 "Add a budget per category and warn when it's exceeded.",
 "Export to CSV so it opens in a spreadsheet."
],
"done":"You can close the program, reopen it, and your expenses are still there. Add, list, delete, total and filter all work, and each lives in its own function."
},

# ───────────────────────────── 03 ─────────────────────────────
{
"num":"03","slug":"03-weather-client","title":"Weather client",
"weeks":"Weeks 5–6","commit":"feat: talk to the internet",
"summary":"Your first program that reaches outside your own machine. APIs, keys, and things going wrong.",
"intro":"""
<p>Everything you've built so far runs entirely on your laptop. This one talks to a server somewhere else, which introduces a whole category of problems: the network fails, the server is slow, the data isn't the shape you expected, and you have a secret key you must not leak.</p>
<p>All of that is normal professional work. This is the project where your code stops being self-contained.</p>
""",
"sessions":[
 {"n":1,"title":"Installing packages, and your first request",
  "teach":"""
<p>Python comes with a lot built in, but not everything. <code>pip</code> installs extra packages into your virtual environment.</p>
<div class="code"><button class="copy">Copy</button><pre><code>source .venv/bin/activate   <span class="c"># always activate first</span>
pip install requests</code></pre></div>
<div class="note warn"><div class="lbl">If pip says it's already installed but Python can't find it</div><p>You've installed into a different environment than the one you're running. Check your prompt starts with <code>(.venv)</code>. This is the most common environment confusion there is.</p></div>
<p>Now make a request:</p>
<div class="code"><button class="copy">Copy</button><pre><code>import requests

response = requests.get("https://api.github.com")
print(response.status_code)   <span class="c"># 200 means OK</span>
print(response.json())</code></pre></div>
<p>Status codes worth knowing: <strong>200</strong> fine, <strong>401</strong> your key is wrong, <strong>404</strong> that doesn't exist, <strong>429</strong> you're asking too often, <strong>500</strong> their problem not yours.</p>
""",
  "build":"<p>Install <code>requests</code>, call any public API, print the status code and the response.</p>",
  "check":"You can install a package and make an HTTP request from Python."},

 {"n":2,"title":"Getting a key, and keeping it secret",
  "teach":"""
<p>Sign up for a free OpenWeatherMap account and get an API key. It's a string that identifies you — treat it exactly like a password.</p>
<p>It must never go in your code, because your code goes on GitHub. Instead, put it in a file called <code>.env</code>:</p>
<div class="code"><button class="copy">Copy</button><pre><code>WEATHER_API_KEY=your_actual_key_here</code></pre></div>
<p>Make sure <code>.env</code> is listed in your <code>.gitignore</code> — check with <code>git status</code>, it should not appear. Then read it in Python:</p>
<div class="code"><button class="copy">Copy</button><pre><code>pip install python-dotenv</code></pre></div>
<div class="code"><button class="copy">Copy</button><pre><code>import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")</code></pre></div>
<p>Also commit a <code>.env.example</code> with the key names but no values, so anyone cloning your repo knows what they need.</p>
<div class="note warn"><div class="lbl">If you commit the key anyway</div><p>It happens. Go to the provider, revoke that key, generate a new one. Don't just delete the line and commit again — it's still in your history, and bots scan public repos for exactly this within minutes.</p></div>
""",
  "build":"<p>Key in <code>.env</code>, <code>.env</code> ignored by git, <code>.env.example</code> committed, key loading correctly in Python.</p>",
  "check":"<code>git status</code> never shows <code>.env</code>, and your program can read the key."},

 {"n":3,"title":"Reading the docs, and query parameters",
  "teach":"""
<p>Nobody memorises APIs. You read the documentation, find the endpoint you need, and work out what to send it.</p>
<p>Extra information goes on the end of a URL as <strong>query parameters</strong> — <code>?city=Manchester&amp;units=metric</code>. <code>requests</code> builds those for you:</p>
<div class="code"><button class="copy">Copy</button><pre><code>params = {
    "q": "Manchester",
    "appid": api_key,
    "units": "metric",
}
response = requests.get(BASE_URL, params=params)</code></pre></div>
<p>That's much safer than gluing strings together, and it handles spaces and odd characters properly.</p>
<div class="note"><div class="lbl">A habit worth forming</div><p>Print the whole response the first time. Don't guess the shape of the data — look at it. <code>print(json.dumps(data, indent=2))</code> makes it readable.</p></div>
""",
  "build":"<p>Fetch real weather for a hardcoded city. Print the raw response and study it before writing anything else.</p>",
  "check":"You can read API docs well enough to construct a working request."},

 {"n":4,"title":"Digging into nested data",
  "teach":"""
<p>API responses are dictionaries inside lists inside dictionaries. Getting a value means walking down through them:</p>
<div class="code"><button class="copy">Copy</button><pre><code>data = response.json()

temperature = data["main"]["temp"]
description = data["weather"][0]["description"]</code></pre></div>
<p>Read that second line as: from <code>data</code>, take the <code>weather</code> key, which is a list; take its first item, which is a dictionary; take the <code>description</code> from that.</p>
<p>Every step is a place it can break. If a field might be missing, <code>.get()</code> won't crash:</p>
<div class="code"><button class="copy">Copy</button><pre><code>wind = data.get("wind", {}).get("speed", "unknown")</code></pre></div>
""",
  "build":"<p>Pull out temperature, description, humidity and wind speed. Print them as a tidy summary. Then make the city a command-line input.</p>",
  "check":"You can navigate nested JSON confidently and know where it might break."},

 {"n":5,"title":"When things go wrong",
  "teach":"""
<p>Your program works. Now try it with the wifi off, with a made-up city, with the key deleted. It'll crash three different ways, and handling that is what separates a script from a tool.</p>
<div class="code"><button class="copy">Copy</button><pre><code>try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
except requests.exceptions.ConnectionError:
    print("Can't reach the weather service. Check your connection.")
except requests.exceptions.Timeout:
    print("The weather service took too long to answer.")
except requests.exceptions.HTTPError:
    if response.status_code == 404:
        print("No city by that name.")
    elif response.status_code == 401:
        print("API key rejected.")
    else:
        print("Something went wrong at their end.")</code></pre></div>
<p>Note the <code>timeout</code>. Without one, your program can hang forever waiting for a server that's never going to answer. Always set one on a network call.</p>
<div class="note"><div class="lbl">What a good error message does</div><p>It says what happened and what to do about it. "Error" says neither. Write them for a person who has no idea how your program works.</p></div>
""",
  "build":"<p>Handle no internet, bad city, bad key and timeout — each with its own message. Test all four deliberately.</p>",
  "check":"Your program never shows a raw traceback to the person using it."},

 {"n":6,"title":"Making it shareable",
  "teach":"""
<p>Someone else needs to be able to run this. Record what it depends on:</p>
<div class="code"><button class="copy">Copy</button><pre><code>pip freeze > requirements.txt</code></pre></div>
<p>Commit that file. Now anyone can recreate your environment with <code>pip install -r requirements.txt</code>.</p>
<p>Check it works by pretending to be them: clone your own repo into a different folder, make a fresh virtual environment, install from the file and run it. This catches things you forgot — it usually catches at least one.</p>
""",
  "build":"<p><code>requirements.txt</code> committed, README covering how to get a key and set up <code>.env</code>, and a genuine clean-clone test.</p>",
  "check":"A stranger could clone your repo and have it running in five minutes."}
],
"traps":[
 ("Assuming the response shape","Print it. Every time. APIs change and documentation lags behind."),
 ("No timeout","A network call without a timeout can hang forever. Always set one."),
 ("Hammering the API while debugging","Free tiers have limits. Save one response to a JSON file and work against that while you build the parsing.")
],
"stretch":[
 "Add a five-day forecast, not just today.",
 "Cache the last response so repeated runs don't re-fetch within a few minutes.",
 "Accept several cities at once and compare them.",
 "Add a <code>--json</code> flag that outputs raw data instead of a summary."
],
"done":"Handles a nonsense city gracefully, key lives in <code>.env</code>, <code>.env</code> is gitignored, <code>requirements.txt</code> is committed, and a clean clone runs first time."
},

# ───────────────────────────── 04 ─────────────────────────────
{
"num":"04","slug":"04-refactor-and-test","title":"Refactor &amp; test",
"weeks":"Weeks 7–8","commit":"refactor: make past-me's code liveable",
"summary":"No new features. Go back to the expense tracker and make it something you'd be happy to hand over.",
"intro":"""
<p>This is the fortnight that feels least like progress and teaches the most. You're not adding anything. You're taking code you wrote a month ago — which you'll find surprisingly hard to read — and restructuring it without breaking it.</p>
<p>That skill, changing existing code safely, is most of what professional engineering actually is. Very little of the job is writing new things on blank pages.</p>
""",
"sessions":[
 {"n":1,"title":"Read your own code",
  "teach":"""
<p>Before changing anything, open the expense tracker and read it start to finish. Keep a notes file open and write down every time you have to stop and work something out.</p>
<p>Look for: functions doing more than one thing, names that don't say what they hold, the same logic copied in two places, functions longer than about twenty lines, and anything you had to re-read twice.</p>
<div class="note"><div class="lbl">This is the exercise</div><p>The discomfort of reading your own old code is the lesson. Every confusing bit is a decision that made sense at the time and doesn't now. That's what you're about to fix — and noticing it is a skill in itself.</p></div>
""",
  "build":"<p>A written list of everything wrong with it. Commit the notes file — it's evidence of how you think, and it'll be satisfying at the end of the fortnight.</p>",
  "check":"You have a concrete list of problems rather than a vague sense the code is messy."},

 {"n":2,"title":"Your first test",
  "teach":"""
<p>Before changing code you need a way to know you haven't broken it. That's what tests are.</p>
<div class="code"><button class="copy">Copy</button><pre><code>pip install pytest</code></pre></div>
<p>A test is a function starting with <code>test_</code> containing an <code>assert</code> — a statement of what should be true:</p>
<div class="code"><button class="copy">Copy</button><pre><code><span class="c"># test_tracker.py</span>
from tracker import calculate_total

def test_total_of_two_expenses():
    expenses = [{"amount": 10.0}, {"amount": 5.50}]
    assert calculate_total(expenses) == 15.50

def test_total_of_empty_list_is_zero():
    assert calculate_total([]) == 0</code></pre></div>
<p>Run them with <code>pytest</code> in your terminal. Green means passing, red means something's wrong.</p>
<p>Each test has three parts: set up the situation, do the thing, check the result. Name tests so a failure tells you what broke without reading the code.</p>
""",
  "build":"<p>Write tests for every function that returns a value. Aim for the normal case, an empty case, and one odd case each.</p>",
  "check":"<code>pytest</code> runs and passes, and you understand what each test is protecting."},

 {"n":3,"title":"The safety net",
  "teach":"""
<p>Tests only help if they cover the behaviour you're about to change. So before refactoring anything, get the current behaviour under test — including the bits you think are ugly.</p>
<p>You'll hit a problem: some functions can't be tested because they do too much. A function that reads input, calculates and prints has no return value to assert on. That's not a testing problem, it's a design problem, and the test is what revealed it.</p>
<div class="note"><div class="lbl">The useful insight</div><p>Hard-to-test code is badly structured code. Testability isn't a separate quality you add — it's a symptom of good separation. If you can't test it, split the calculating from the printing and test the calculating.</p></div>
<p>Test what the function <em>does</em>, not how it does it. A test that breaks when you rename an internal variable is a test that will annoy you forever.</p>
""",
  "build":"<p>Every calculation function under test. Split any function that mixes input, logic and output — logic in the middle, testable.</p>",
  "check":"You can change the inside of any calculation function and the tests will tell you if you broke it."},

 {"n":4,"title":"Classes",
  "teach":"""
<p>You've been passing the same list of expenses into every function. A <strong>class</strong> bundles data together with the functions that work on it.</p>
<div class="code"><button class="copy">Copy</button><pre><code>class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, description, amount, category):
        self.expenses.append({
            "description": description,
            "amount": amount,
            "category": category,
        })

    def total(self):
        return sum(e["amount"] for e in self.expenses)</code></pre></div>
<div class="code"><button class="copy">Copy</button><pre><code>book = ExpenseBook()
book.add("Coffee", 3.40, "food")
print(book.total())</code></pre></div>
<p><code>__init__</code> runs when you create one. <code>self</code> means "this particular book" — it's how each instance keeps its own data. Functions inside a class are called methods.</p>
<p>Classes aren't automatically better. They're useful when data and behaviour belong together — which is exactly the case here.</p>
""",
  "build":"<p>Rebuild the tracker around an <code>ExpenseBook</code> class. Keep the tests green the whole way through.</p>",
  "check":"You can explain what <code>self</code> does without reciting a definition."},

 {"n":5,"title":"Splitting into files",
  "teach":"""
<p>One long file is fine until it isn't. Split by responsibility:</p>
<div class="code"><pre><code>expense_tracker/
  main.py         <span class="c"># menu loop, talks to the person</span>
  expense_book.py <span class="c"># the class, all the logic</span>
  storage.py      <span class="c"># loading and saving JSON</span>
  test_book.py
  test_storage.py</code></pre></div>
<p>Import across files by filename:</p>
<div class="code"><button class="copy">Copy</button><pre><code>from expense_book import ExpenseBook
from storage import load, save</code></pre></div>
<p>The division that matters: <code>main.py</code> is the only file that talks to a human. Everything else just works with data. That's why the rest is testable — and it's the same separation that will let you put a web interface on it in project 5 without rewriting the logic.</p>
""",
  "build":"<p>Split into modules. Tests still green. Everything still works.</p>",
  "check":"Your logic files contain no <code>print</code> or <code>input</code> at all."},

 {"n":6,"title":"Refactor for real",
  "teach":"""
<p>Now the safety net is in place, go through your week-one list of problems and fix them properly. The discipline:</p>
<ol>
<li>Make one small change</li>
<li>Run the tests</li>
<li>Green? Commit. Red? Undo it and go smaller.</li>
</ol>
<p>Never make two changes at once. When something breaks you want to know exactly what caused it.</p>
<div class="note warn"><div class="lbl">The temptation to start over</div><p>At some point you'll want to delete it and rewrite from scratch. Don't. Rewriting is easy and teaches you nothing; changing working code without breaking it is the actual skill, and it's the one you'll use every week of your career.</p></div>
""",
  "build":"<p>Work through the list. Commit after each fix. Finish by re-reading the file you wrote in session 1 and adding a note on what changed.</p>",
  "check":"15+ tests pass, the code is across several files, and you ran the tests before every commit."}
],
"traps":[
 ("Deleting and rewriting","Not refactoring. The skill is changing code safely, in steps, with the tests green."),
 ("Testing the inside","If renaming a private variable breaks a test, the test is testing the wrong thing. Test behaviour."),
 ("Classes everywhere","Not everything needs to be a class. A function that takes some data and returns an answer is often just better.")
],
"stretch":[
 "Add a test that checks loading and saving round-trips correctly.",
 "Use <code>pytest</code> fixtures to avoid repeating setup in every test.",
 "Add type hints to your functions and run <code>mypy</code> over it.",
 "Set up GitHub Actions to run your tests automatically on every push."
],
"done":"15+ passing tests, code split across modules, no printing inside the logic, and a commit history showing small steps rather than one giant rewrite."
},

# ───────────────────────────── 05 ─────────────────────────────
{
"num":"05","slug":"05-first-web-app","title":"First web app",
"weeks":"Weeks 9–10","commit":"feat: it has a URL now",
"summary":"The same tracker, but in a browser. Flask, HTML, forms, and the request cycle.",
"intro":"""
<p>Everything so far has run in a terminal. Now you'll put a web interface on it — and because you separated the logic from the interface in project 4, most of your code carries over untouched. That's the payoff for the fortnight that felt like no progress.</p>
""",
"sessions":[
 {"n":1,"title":"What actually happens when you visit a page",
  "teach":"""
<p>You type a URL. Your browser sends a <strong>request</strong> to a server. The server sends back a <strong>response</strong>, usually HTML. Your browser draws it. Then the connection closes and the server forgets you exist.</p>
<p>That last part matters: the web is stateless. Every request stands alone. Anything remembered between requests has to be deliberately stored — which is why sessions and databases exist.</p>
<div class="code"><button class="copy">Copy</button><pre><code>pip install flask</code></pre></div>
<div class="code"><button class="copy">Copy</button><pre><code>from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask"

if __name__ == "__main__":
    app.run(debug=True)</code></pre></div>
<p>Run it and visit <code>localhost:5000</code>. The <code>@app.route("/")</code> line says "when someone asks for the root URL, run this function". <code>debug=True</code> reloads on save and shows errors in the browser — helpful now, dangerous in production.</p>
""",
  "build":"<p>Flask running locally with two routes: <code>/</code> and <code>/about</code>.</p>",
  "check":"You can explain what a request and a response are, and add a new route."},

 {"n":2,"title":"Enough HTML",
  "teach":"""
<p>HTML describes structure. Tags wrap content, most come in pairs.</p>
<div class="code"><button class="copy">Copy</button><pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;Expenses&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;My expenses&lt;/h1&gt;
  &lt;p&gt;A paragraph.&lt;/p&gt;
  &lt;ul&gt;
    &lt;li&gt;Coffee — £3.40&lt;/li&gt;
  &lt;/ul&gt;
  &lt;a href="/add"&gt;Add one&lt;/a&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre></div>
<p>The dozen tags you need: <code>h1</code>–<code>h3</code> headings, <code>p</code> paragraph, <code>ul</code>/<code>li</code> lists, <code>a</code> links, <code>div</code> generic container, <code>form</code>/<code>input</code>/<code>button</code> for input, <code>table</code>/<code>tr</code>/<code>td</code> for tables.</p>
<p>Flask looks for HTML files in a folder called <code>templates</code>:</p>
<div class="code"><button class="copy">Copy</button><pre><code>from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")</code></pre></div>
""",
  "build":"<p>A <code>templates/index.html</code> with a heading and a hardcoded list, served by Flask.</p>",
  "check":"You can write basic HTML and serve it from a route."},

 {"n":3,"title":"Templates with real data",
  "teach":"""
<p>Hardcoded HTML is no use. <strong>Jinja</strong> lets you put Python-ish logic in your templates.</p>
<div class="code"><button class="copy">Copy</button><pre><code>@app.route("/")
def home():
    expenses = book.all()
    return render_template("index.html", expenses=expenses)</code></pre></div>
<div class="code"><button class="copy">Copy</button><pre><code>&lt;ul&gt;
{% raw %}{% for e in expenses %}
  &lt;li&gt;{{ e.description }} — £{{ e.amount }}&lt;/li&gt;
{% endfor %}{% endraw %}
&lt;/ul&gt;

{% raw %}{% if not expenses %}
  &lt;p&gt;Nothing yet. Add your first expense.&lt;/p&gt;
{% endif %}{% endraw %}</code></pre></div>
<p>Double curly braces print a value. Curly-brace-percent is a statement — a loop or a condition. Note the empty state: an empty screen should tell someone what to do next.</p>
""",
  "build":"<p>Real expenses from your <code>ExpenseBook</code> rendered in the page, with a sensible empty state.</p>",
  "check":"You can pass data from a route into a template and loop over it."},

 {"n":4,"title":"Forms, and getting data back",
  "teach":"""
<p>So far data flows one way. A form sends it back.</p>
<div class="code"><button class="copy">Copy</button><pre><code>&lt;form action="/add" method="POST"&gt;
  &lt;input type="text" name="description" required&gt;
  &lt;input type="number" name="amount" step="0.01" required&gt;
  &lt;button type="submit"&gt;Add&lt;/button&gt;
&lt;/form&gt;</code></pre></div>
<p><strong>GET</strong> asks for something. <strong>POST</strong> sends something that changes state. Use POST for anything that adds, edits or deletes.</p>
<div class="code"><button class="copy">Copy</button><pre><code>from flask import request, redirect, url_for

@app.route("/add", methods=["POST"])
def add():
    description = request.form["description"]
    amount = float(request.form["amount"])
    book.add(description, amount, "general")
    return redirect(url_for("home"))</code></pre></div>
<div class="note"><div class="lbl">Why redirect after a POST</div><p>If you render a page directly from a POST, refreshing re-submits the form and adds the expense twice. Redirecting sends the browser to a fresh GET, so refreshing is harmless. This pattern has a name — post/redirect/get — and forgetting it causes duplicate-submission bugs everywhere.</p></div>
""",
  "build":"<p>A working add form, and a delete button on each row. Both POST, both redirect.</p>",
  "check":"You can take form input, act on it, and redirect properly."},

 {"n":5,"title":"Enough CSS",
  "teach":"""
<p>Put a stylesheet at <code>static/style.css</code> and link it:</p>
<div class="code"><button class="copy">Copy</button><pre><code>{% raw %}&lt;link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"&gt;{% endraw %}</code></pre></div>
<p>Ninety per cent of "looks fine" comes from four things: a readable font, a max width so lines aren't enormous, consistent spacing, and enough contrast.</p>
<div class="code"><button class="copy">Copy</button><pre><code>body {
  font-family: system-ui, sans-serif;
  max-width: 700px;
  margin: 40px auto;
  padding: 0 20px;
  line-height: 1.6;
  color: #222;
}</code></pre></div>
<div class="note warn"><div class="lbl">Four hours, then stop</div><p>CSS is genuinely absorbing and will eat your fortnight if you let it. Set a timer. Make it clean and legible, then go back to the parts that teach you more.</p></div>
""",
  "build":"<p>Styled well enough that you'd show someone. Not beautiful. Legible and tidy.</p>",
  "check":"It doesn't look like an unstyled 1998 web page, and you spent under four hours on that."},

 {"n":6,"title":"Joining it up",
  "teach":"""
<p>Pull the whole thing together: list, add, delete, filter by category, a total at the top.</p>
<p>Keep the separation you built in project 4 — routes handle web things (reading the form, redirecting), the <code>ExpenseBook</code> handles logic. If you find yourself calculating totals inside a route, move it.</p>
<p>Reuse the shared layout rather than repeating your header in every file:</p>
<div class="code"><button class="copy">Copy</button><pre><code>{% raw %}&lt;!-- base.html --&gt;
&lt;body&gt;
  &lt;h1&gt;Expenses&lt;/h1&gt;
  {% block content %}{% endblock %}
&lt;/body&gt;

&lt;!-- index.html --&gt;
{% extends "base.html" %}
{% block content %}
  ...the page...
{% endblock %}{% endraw %}</code></pre></div>
""",
  "build":"<p>Full working app. README with a screenshot — use <code>⇧⌘4</code> to grab one.</p>",
  "check":"All the terminal features work in a browser, and your logic code has no Flask in it."}
],
"traps":[
 ("The CSS rabbit hole","Four hours. Timer on."),
 ("Logic inside routes","A route should read the request, call your logic, and return a response. If it's doing maths, move it."),
 ("Rendering straight from a POST","Refresh re-submits. Redirect instead.")
],
"stretch":[
 "Add an edit page for an existing expense.",
 "Add flash messages confirming an action worked.",
 "Make it usable on a phone with a CSS media query.",
 "Add a chart of spending by category with a JavaScript charting library."
],
"done":"Runs at <code>localhost:5000</code>, you can add and delete in a browser, refreshing never duplicates anything, and it looks deliberately made."
},

# ───────────────────────────── 06 ─────────────────────────────
{
"num":"06","slug":"06-database-and-deploy","title":"Database &amp; deploy",
"weeks":"Weeks 11–12","commit":"feat: real database, live on the internet",
"summary":"Swap the JSON file for SQL, then put the whole thing on the internet.",
"intro":"""
<p>Two milestones in one fortnight. First a real database, because a JSON file falls apart the moment two people use it at once. Then deployment — the first thing you've built that someone else can open on their phone.</p>
<p>Expect the deployment day to be frustrating. It is for everyone, every time.</p>
""",
"sessions":[
 {"n":1,"title":"SQL basics",
  "teach":"""
<p>SQLite comes with Python and stores a whole database in one file. Open one in your terminal:</p>
<div class="code"><button class="copy">Copy</button><pre><code>sqlite3 expenses.db</code></pre></div>
<p>Data lives in <strong>tables</strong> — columns define what a row can hold:</p>
<div class="code"><button class="copy">Copy</button><pre><code>CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);</code></pre></div>
<p><code>PRIMARY KEY</code> means unique identifier, filled in automatically. <code>NOT NULL</code> means required.</p>
<div class="code"><button class="copy">Copy</button><pre><code>INSERT INTO expenses (description, amount, category)
VALUES ('Coffee', 3.40, 'food');

SELECT * FROM expenses;
SELECT * FROM expenses WHERE category = 'food';
SELECT * FROM expenses ORDER BY amount DESC;
SELECT SUM(amount) FROM expenses;
SELECT category, SUM(amount) FROM expenses GROUP BY category;</code></pre></div>
<p>That last one is worth sitting with. <code>GROUP BY</code> collapses rows into groups and calculates across each — it's how every "spending by category" report ever built works.</p>
""",
  "build":"<p>Create the table by hand, insert ten rows, and write queries answering: what did I spend in total, what's my biggest expense, what's the total per category.</p>",
  "check":"You can write SELECT, INSERT, WHERE, ORDER BY and GROUP BY from memory."},

 {"n":2,"title":"SQL from Python — and injection",
  "teach":"""
<div class="code"><button class="copy">Copy</button><pre><code>import sqlite3

conn = sqlite3.connect("expenses.db")
conn.row_factory = sqlite3.Row     <span class="c"># get dict-like rows</span>
cursor = conn.cursor()

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

conn.commit()   <span class="c"># needed after INSERT/UPDATE/DELETE</span>
conn.close()</code></pre></div>
<p>Now the most important thing in this entire fortnight. <strong>Never build a query by joining strings.</strong></p>
<div class="code"><button class="copy">Copy</button><pre><code><span class="c"># NEVER do this</span>
cursor.execute(f"SELECT * FROM expenses WHERE category = '{category}'")

<span class="c"># do this</span>
cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))</code></pre></div>
<div class="note warn"><div class="lbl">Why this matters</div><p>In the first version, someone typing <code>' OR '1'='1</code> as a category changes what your query means and gets everything back. Worse inputs delete tables. This is SQL injection, it's been in the top ten web vulnerabilities for twenty years, and the fix is simply always using <code>?</code> placeholders. Look up "Little Bobby Tables" for the famous version.</p></div>
<p>The comma in <code>(category,)</code> isn't a typo — it makes it a tuple of one item.</p>
""",
  "build":"<p>A <code>database.py</code> with functions to add, list, delete and total, all using placeholders.</p>",
  "check":"You can explain SQL injection and you've written no query using an f-string."},

 {"n":3,"title":"Swapping the storage out",
  "teach":"""
<p>Replace JSON with SQL inside your storage layer. If project 4 went well, nothing else has to change — the rest of the app doesn't know or care where data comes from.</p>
<p>That's the payoff for separating concerns, and it's worth noticing when it happens. If you <em>do</em> have to change the routes and the templates too, that tells you the layers were more tangled than you thought. Useful information either way.</p>
<p>Write a small script to create the table if it doesn't exist, so a fresh clone works:</p>
<div class="code"><button class="copy">Copy</button><pre><code>def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(&quot;&quot;&quot;CREATE TABLE IF NOT EXISTS expenses (...)&quot;&quot;&quot;)
    conn.commit()
    conn.close()</code></pre></div>
""",
  "build":"<p>App fully on SQLite. Tests updated and green. JSON code deleted.</p>",
  "check":"Only your storage layer changed, and you can articulate why that's a good sign."},

 {"n":4,"title":"Getting ready to deploy",
  "teach":"""
<p>Your laptop and a server differ in ways that will bite you. Fix them before deploying, not after.</p>
<ul>
<li><strong>Debug off.</strong> <code>debug=True</code> shows your source code to anyone who triggers an error. Read the mode from an environment variable.</li>
<li><strong>No hardcoded paths.</strong> <code>/Users/you/code/...</code> doesn't exist on a server.</li>
<li><strong>Port from the environment.</strong> The host decides, not you: <code>port = int(os.environ.get("PORT", 5000))</code></li>
<li><strong>A real web server.</strong> Flask's built-in one is for development only. <code>pip install gunicorn</code>.</li>
<li><strong>Requirements current.</strong> <code>pip freeze &gt; requirements.txt</code></li>
</ul>
<div class="note"><div class="lbl">SQLite in production</div><p>Most hosts wipe the filesystem on restart, which takes your database with it. Fine for a demo; use the host's managed Postgres if you want the data to survive. Either is a legitimate choice — just make it knowingly.</p></div>
""",
  "build":"<p>Everything configurable via environment variables. Nothing hardcoded. Runs locally under gunicorn.</p>",
  "check":"Nothing in your code assumes it's on your laptop."},

 {"n":5,"title":"Deploying",
  "teach":"""
<p>Pick a host with a free tier — Render, Railway and Fly.io all work. Connect your GitHub repo, set the environment variables in their dashboard, and let it build.</p>
<p>It will probably fail. That's normal and the logs will tell you why. Common causes:</p>
<ul>
<li>A package missing from <code>requirements.txt</code> because you installed it and forgot to freeze</li>
<li>Wrong start command — usually <code>gunicorn app:app</code></li>
<li>Ignoring the platform's <code>PORT</code> variable</li>
<li>An environment variable set locally but never added to the host</li>
</ul>
<div class="note"><div class="lbl">How to debug a failed deploy</div><p>Read the build log from the top, not the bottom. The first error is the real one; everything after is fallout. This is true of almost every log you'll ever read.</p></div>
""",
  "build":"<p>A live URL. Send it to three people and watch someone use it on a phone.</p>",
  "check":"Someone who isn't you has opened your app on a device that isn't yours."},

 {"n":6,"title":"After it's live",
  "teach":"""
<p>Watch someone use it without helping. You'll learn more in five minutes than in a week of guessing.</p>
<p>Then tidy: fix whatever they got confused by, check it works on a phone screen, make sure an error shows a friendly page rather than a stack trace, and put the live link at the very top of your README.</p>
<p>Take a moment on this one. Twelve weeks ago you couldn't open a terminal.</p>
""",
  "build":"<p>Live link in the README, a screenshot, and a note on what you'd do differently.</p>",
  "check":"It works on a phone and doesn't leak stack traces to strangers."}
],
"traps":[
 ("f-strings in SQL","Always <code>?</code> placeholders. No exceptions, ever."),
 ("Debug mode in production","Shows your source code to the world. Off."),
 ("Committing the database file","Add <code>*.db</code> to <code>.gitignore</code>."),
 ("Assuming deploy will be quick","Set aside a whole session and expect to spend it reading logs.")
],
"stretch":[
 "Add a second table for categories with a foreign key, and JOIN them.",
 "Add a monthly summary page with GROUP BY on the date.",
 "Add a custom 404 page.",
 "Set up automatic deploys on every push to main."
],
"done":"Someone else can open your app on their phone. Data is in a real database, every query uses placeholders, and debug mode is off."
},

# ───────────────────────────── 07 ─────────────────────────────
{
"num":"07","slug":"07-accounts-and-auth","title":"Accounts &amp; auth",
"weeks":"Weeks 13–14","commit":"feat: multiple users, real accounts",
"summary":"Your portfolio piece. Something you'd actually use, with real user accounts.",
"intro":"""
<p>This is the project you'll talk about in interviews, so build something you care about — a habit tracker, a reading log, a five-a-side organiser, a recipe box, a running log. It only has to matter to you.</p>
<p>By week 13 the novelty has completely gone. Genuine interest in what you're building is what gets you through the fortnight.</p>
""",
"sessions":[
 {"n":1,"title":"Design before you build",
  "teach":"""
<p>Start on paper. What are the things in your app, what does each one need to know, and how do they relate?</p>
<p>For a reading log: a <strong>user</strong> has an email and a password hash; a <strong>book</strong> has a title, an author, a status and a rating — and belongs to a user.</p>
<p>That "belongs to" is a <strong>foreign key</strong> — a column holding another table's id:</p>
<div class="code"><button class="copy">Copy</button><pre><code>CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'to-read',
    FOREIGN KEY (user_id) REFERENCES users(id)
);</code></pre></div>
<p>Sketch the pages too. Four or five is plenty: sign up, log in, the main list, add, edit.</p>
""",
  "build":"<p>A written data model and a rough sketch of each page. Commit it — deciding before building is the professional habit.</p>",
  "check":"You can explain your tables and how they relate before writing any code."},

 {"n":2,"title":"Passwords, done properly",
  "teach":"""
<p>You never store a password. You store a <strong>hash</strong> — a one-way transformation that can't be reversed. When someone logs in, you hash what they typed and compare hashes.</p>
<div class="code"><button class="copy">Copy</button><pre><code>from werkzeug.security import generate_password_hash, check_password_hash

hashed = generate_password_hash(password)      <span class="c"># on sign-up</span>
ok = check_password_hash(hashed, attempt)      <span class="c"># on log-in</span></code></pre></div>
<p>That's the whole thing. The library handles salting and choosing a slow algorithm — both of which matter and neither of which you should implement yourself.</p>
<div class="note warn"><div class="lbl">Why this is worth understanding, not just copying</div><p>Databases leak. Regularly. If yours leaks with plain-text passwords, you've handed over credentials that many people reuse on their email and their bank. Hashing means an attacker gets a pile of useless strings instead. It's the difference between an embarrassing incident and a serious one.</p></div>
<p>Hashing is one-way; encryption is two-way. Passwords are hashed. If you ever meet a service that can email you your existing password, they've done it wrong.</p>
""",
  "build":"<p>Working sign-up: form, validation, hash, store. Check the database — you should see gibberish where the passwords are.</p>",
  "check":"You can explain hashing versus encryption, and why salting exists."},

 {"n":3,"title":"Logging in, and staying logged in",
  "teach":"""
<p>HTTP forgets you between requests, so after a successful log-in you store something in a <strong>session</strong> — a small signed cookie Flask manages for you.</p>
<div class="code"><button class="copy">Copy</button><pre><code>from flask import session

<span class="c"># after checking the password</span>
session["user_id"] = user["id"]

<span class="c"># logging out</span>
session.clear()</code></pre></div>
<p>Flask signs the cookie with your <code>SECRET_KEY</code> so nobody can tamper with it. Generate a real random one and keep it in your environment variables — never in the code.</p>
<div class="note warn"><div class="lbl">Vague log-in errors are deliberate</div><p>Say "email or password is incorrect", never "no account with that email". The second version lets someone test which addresses are registered. This is called user enumeration and it's worth knowing the name.</p></div>
""",
  "build":"<p>Log in, log out, and a page that shows who you are when you're logged in.</p>",
  "check":"You can log in, close the tab, come back and still be logged in — and explain what's in the cookie."},

 {"n":4,"title":"Protecting pages",
  "teach":"""
<p>Now stop logged-out people reaching pages they shouldn't. A <strong>decorator</strong> lets you mark routes as protected:</p>
<div class="code"><button class="copy">Copy</button><pre><code>from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapped

@app.route("/books")
@login_required
def books():
    ...</code></pre></div>
<p>Decorators look strange the first time. All this one does is wrap your function in a check that runs first.</p>
""",
  "build":"<p>Every page that shows or changes data requires a login. Test by logging out and typing the URL directly.</p>",
  "check":"There's no URL a logged-out person can reach that shows anything private."},

 {"n":5,"title":"The bug almost everyone ships",
  "teach":"""
<p>Log in as user A, open one of your items, and look at the URL — <code>/books/7</code>. Now log in as user B and type that same URL.</p>
<p>If you can see user A's book, you have an <strong>IDOR</strong> — insecure direct object reference. You checked whether someone was logged in, but never whether <em>this</em> logged-in person owns <em>that</em> record.</p>
<div class="code"><button class="copy">Copy</button><pre><code><span class="c"># not enough</span>
"SELECT * FROM books WHERE id = ?"

<span class="c"># correct</span>
"SELECT * FROM books WHERE id = ? AND user_id = ?"</code></pre></div>
<p>Every query touching user data needs that second condition. Authentication is who you are; authorisation is what you're allowed to touch. Confusing them is one of the most common real-world security holes there is.</p>
""",
  "build":"<p>Audit every route. Create two accounts and genuinely try to break into one from the other — including edit and delete, not just viewing.</p>",
  "check":"Two accounts, tested by hand, and no URL exposes anyone else's data."},

 {"n":6,"title":"Finish and deploy",
  "teach":"""
<p>Deploy it, then write the README as though a hiring manager will read it — because one might.</p>
<p>Cover: what it does and why you built it, a screenshot, the live link, how to run it locally, the data model, and an honest "what I'd do differently". That last section is the one that makes people take you seriously.</p>
<p>Add test accounts to the README so someone can look around without signing up.</p>
""",
  "build":"<p>Deployed, README written properly, link sent to someone who'll actually use it.</p>",
  "check":"Live, secure, and documented well enough to show a stranger."}
],
"traps":[
 ("Writing your own password hashing","Use the library. Then read about why."),
 ("Checking login but not ownership","The IDOR bug. Test it with two accounts, by hand, every time."),
 ("SECRET_KEY in the code","Environment variable. If it leaks, sessions can be forged."),
 ("Building something you don't care about","Week 13 is late. Motivation has to come from the project itself.")
],
"stretch":[
 "Add a password reset flow via email.",
 "Add rate limiting on log-in attempts.",
 "Let users share one item publicly with a secret link.",
 "Add pagination once there are more than about fifty rows."
],
"done":"Two accounts see two different sets of data, passwords are hashed, no URL leaks another user's records, and it's live."
},

# ───────────────────────────── 08 ─────────────────────────────
{
"num":"08","slug":"08-add-a-brain","title":"Add a brain",
"weeks":"Weeks 15–16","commit":"feat: build something with a language model",
"summary":"An AI feature that survives the model being slow, wrong, or unavailable.",
"intro":"""
<p>Calling a language model API is easy — it's a few lines. The engineering is everything around it: what happens when it's slow, when it returns something malformed, when it's confidently wrong, and when it costs more than you expected.</p>
<p>That's what this fortnight is about. The API call is the least interesting part.</p>
""",
"sessions":[
 {"n":1,"title":"Your first model call",
  "teach":"""
<p>Get an API key from Anthropic or OpenAI, put it in <code>.env</code>, and set a spending cap on the account before you write a line of code.</p>
<div class="code"><button class="copy">Copy</button><pre><code>import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "Categorise this expense: 'Coffee at Pret'"}],
)
print(message.content[0].text)</code></pre></div>
<p>You pay per <strong>token</strong> — roughly a word-and-a-bit. Both what you send and what comes back. <code>max_tokens</code> caps the reply length, which caps the cost.</p>
<div class="note machine"><div class="lbl">Hosted, not local</div><p>You can't run a useful model on 8GB of memory. That's a hardware limit, not a skill one — and hosted APIs are what nearly all production systems use anyway. A project like this costs pennies.</p></div>
""",
  "build":"<p>A script that sends a prompt and prints the answer. Check your usage dashboard afterwards to see what it cost.</p>",
  "check":"You can call the API, and you know how you're being charged."},

 {"n":2,"title":"Prompts as inputs you design",
  "teach":"""
<p>A prompt is an input to your program, so treat it with the same care. Vague prompts give inconsistent output, and inconsistent output is unusable in code.</p>
<p>What helps: be specific about the task, state the exact options, give an example, and say what to do when unsure.</p>
<div class="code"><button class="copy">Copy</button><pre><code>prompt = f&quot;&quot;&quot;Categorise this expense into exactly one category.

Categories: food, travel, bills, entertainment, other

Rules:
- Reply with the category name only, nothing else
- If genuinely unclear, reply: other

Expense: {description}&quot;&quot;&quot;</code></pre></div>
<p>Test it against fifteen or twenty real descriptions, including deliberately awkward ones. You're looking for consistency, not cleverness.</p>
<p>The <code>system</code> parameter sets standing behaviour; the user message carries the specific task. Keep the instructions in the system prompt and the data in the user message — it makes both easier to change.</p>
""",
  "build":"<p>A prompt that categorises reliably across twenty test cases. Keep the awkward ones in a file — they're your test suite.</p>",
  "check":"The same input gives the same category, and you've seen where it struggles."},

 {"n":3,"title":"Structured output, and never trusting it",
  "teach":"""
<p>Prose is no use to a program. Ask for JSON:</p>
<div class="code"><button class="copy">Copy</button><pre><code>prompt = &quot;&quot;&quot;Return only valid JSON, no other text:
{"category": "food|travel|bills|entertainment|other",
 "confidence": "high|medium|low"}&quot;&quot;&quot;</code></pre></div>
<p>Then treat what comes back as untrusted input, because that's exactly what it is:</p>
<div class="code"><button class="copy">Copy</button><pre><code>import json

VALID = {"food", "travel", "bills", "entertainment", "other"}

def parse_response(text):
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {"category": "other", "confidence": "low"}

    if data.get("category") not in VALID:
        return {"category": "other", "confidence": "low"}

    return data</code></pre></div>
<div class="note warn"><div class="lbl">This is the whole lesson</div><p>Models return malformed JSON, invent categories you never offered, and wrap answers in explanation you didn't ask for. Always validate. Always have a fallback. Code that assumes a well-formed response will break in production, and it'll break on a Saturday.</p></div>
""",
  "build":"<p>Structured output with full validation. Force failures by asking for nonsense and make sure your fallback holds.</p>",
  "check":"Your app cannot be broken by the model returning something unexpected."},

 {"n":4,"title":"Wiring it into the app",
  "teach":"""
<p>Add the feature to project 7. Keep the model call in its own module — a function that takes text and returns a validated result. Your routes shouldn't know which provider you're using.</p>
<div class="code"><button class="copy">Copy</button><pre><code><span class="c"># ai.py</span>
def suggest_category(description: str) -> str:
    ...returns a valid category, always...</code></pre></div>
<p>That separation means you can swap providers, or replace it with a fixed answer in your tests, without touching the rest of the app. Tests that call a real API are slow, flaky and cost money.</p>
<div class="note"><div class="lbl">Make it a suggestion, not a decision</div><p>Pre-fill the category and let the person change it. AI features that quietly decide things are infuriating when they're wrong — and they will sometimes be wrong.</p></div>
""",
  "build":"<p>The AI feature working inside your app, in its own module, with tests that don't hit the real API.</p>",
  "check":"You could swap providers by changing one file."},

 {"n":5,"title":"Slow, broken, and expensive",
  "teach":"""
<p>Model calls take seconds, not milliseconds. Without a loading state your app looks frozen and people click twice.</p>
<div class="code"><button class="copy">Copy</button><pre><code>try:
    result = suggest_category(description)
except APITimeoutError:
    result = None          <span class="c"># carry on without it</span>
except APIError:
    result = None</code></pre></div>
<p>The pattern that matters: <strong>the AI feature failing must not break the app.</strong> If the model is down, adding an expense should still work — just without a suggested category. Degrade, don't collapse.</p>
<p>On cost: set a spending cap, keep <code>max_tokens</code> tight, don't send more context than you need, and cache repeated inputs. If someone adds "Coffee" fifty times you shouldn't pay fifty times.</p>
""",
  "build":"<p>Loading state, timeout handling, graceful degradation, and a simple cache. Test with the API key deliberately wrong.</p>",
  "check":"Break the API on purpose and the rest of the app carries on."},

 {"n":6,"title":"Ship it, and look back",
  "teach":"""
<p>Deploy with the key in the host's environment variables. Check the loading state on a slow phone connection. Watch the costs for a few days.</p>
<p>Then write the final README — and this one deserves proper effort. What the feature does, what you learned about prompting, how you handle failure, what it costs to run, what you'd do differently.</p>
<p>Then go and read the code you wrote in week one. Sixteen weeks ago you were working out what a variable was.</p>
""",
  "build":"<p>Deployed and documented. Then update your portfolio index so all eight projects link together.</p>",
  "check":"Live, resilient, and explained well enough that someone can tell what you understand."}
],
"traps":[
 ("Trusting the output","Validate everything. Always have a fallback."),
 ("No timeout","A hanging model call hangs your whole page."),
 ("Letting AI failure break the app","The feature is optional. The app isn't."),
 ("No spending cap","Set one before your first call, not after your first bill.")
],
"stretch":[
 "Stream the response so text appears as it's generated.",
 "Let the person correct a suggestion and store the correction.",
 "Add a natural-language search over their own data.",
 "Log every prompt and response so you can debug odd behaviour later."
],
"done":"Deployed, key in environment variables, survives the API failing, has a loading state, and has a spending cap on the account."
},

]
