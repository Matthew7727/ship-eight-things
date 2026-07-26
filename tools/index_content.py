# -*- coding: utf-8 -*-
from projects import PROJECTS

def spine():
    out = ['<div class="spine">']
    for i, p in enumerate(PROJECTS):
        ai = " ai" if p["num"] == "08" else ""
        out.append(f'''<article class="commit{ai}">
  <a class="card" href="projects/{p["slug"]}.html">
    <div class="chead"><span class="cnum">{p["num"]}</span><span class="ctitle">{p["title"]}</span><span class="cweeks">{p["weeks"].lower()}</span></div>
    <div class="cmsg">{p["commit"]}</div>
    <p>{p["summary"]}</p>
    <span class="go">Open the guide &rarr;</span>
  </a>
</article>''')
    out.append('</div>')
    return "\n".join(out)


INDEX_BODY = """
<section id="how">
  <div class="eyebrow">Start here</div>
  <h2>How this works</h2>
  <p class="lede">Four months. Eight projects. Everything you build goes on GitHub the day you start it, not the day it's finished.</p>
  <p>There are no exercises in this guide. No puzzles, no drills, no fake problems with tidy answers. You learn by building things that don't work yet and making them work.</p>
  <p>Each project is chosen so the next one is impossible without learning something new. Project 2 will lose all your data when you close it &mdash; that's how you end up learning file storage. Project 4 makes you go back and fix your own mess from week 3 &mdash; that's how you learn why structure matters. The frustration is the curriculum.</p>

  <h3>The rules</h3>
  <ul>
    <li><strong>Everything gets committed.</strong> Broken code, half-finished code, embarrassing code. Every session ends with a commit and a push.</li>
    <li><strong>Every project gets a README.</strong> Written for someone who's never seen it. This is not admin &mdash; writing about code is how you find out whether you understood it.</li>
    <li><strong>You must be able to explain every line you commit.</strong> Not "it works." Why it works. If you can't, it doesn't get committed yet.</li>
    <li><strong>Finished beats perfect.</strong> Eight shipped, scruffy projects beat two immaculate ones. Move on when the definition of done is met.</li>
  </ul>

  <div class="note">
    <div class="lbl">What you'll have at the end</div>
    <p>Eight repositories with four months of daily commit history. At least three applications live on the internet with real URLs. A working understanding of Python, the terminal, git, HTTP, SQL, deployment, and building with language models &mdash; all of it learned by needing it, not by being told about it.</p>
  </div>
</section>

<section id="rhythm">
  <div class="eyebrow">Start here</div>
  <h2>The weekly rhythm</h2>
  <p>Around 15&ndash;20 hours a week, across evenings and weekends. The shape matters more than the exact hours.</p>
  <table>
    <tr><th>When</th><th>Roughly</th><th>What</th></tr>
    <tr><td>Two or three weeknights</td><td>2 hrs each</td><td>Build. Small, focused sessions. End each one with a commit.</td></tr>
    <tr><td>One weekend block</td><td>4&ndash;5 hrs</td><td>The heavy lifting &mdash; new concepts, the hard bits, the parts that need a run-up.</td></tr>
    <tr><td>One weekend session</td><td>90 mins</td><td>Pairing. You drive, your mentor navigates. Then swap.</td></tr>
    <tr><td>Sunday, before you stop</td><td>20 mins</td><td>Update the README. Push everything. Write down what confused you this week.</td></tr>
  </table>
  <p>Each project spans two weeks and is broken into six sessions. That's deliberately one more session than a fortnight strictly allows &mdash; things overrun, and the slack is built in.</p>
  <div class="note warn">
    <div class="lbl">The weeks people quit</div>
    <p>Weeks 3, 7 and 11 are where this normally falls apart. The novelty has gone, the thing you're building is ugly, and progress feels invisible. It isn't &mdash; go back and read your week 1 code. Keep the sessions short and frequent rather than heroic and rare. Two hours on a Tuesday beats a guilty eight-hour Sunday.</p>
  </div>
</section>

<section id="machine">
  <div class="eyebrow">Setup</div>
  <h2>Your machine</h2>
  <p>The MacBook Neo runs an A18 Pro chip &mdash; the first Mac to use Apple's phone-and-tablet silicon rather than an M-series chip &mdash; with 8GB of memory. For everything in this guide, that's a perfectly capable development machine. The processor is not going to be your limit.</p>
  <p><strong>The memory is.</strong> 8GB is the constraint that shapes a few decisions, and it's worth knowing now rather than discovering it in month three when everything mysteriously starts crawling.</p>

  <div class="note machine">
    <div class="lbl">Four calls made for this machine</div>
    <p><strong>Skip Docker Desktop.</strong> It's a memory hog and you don't need containers for anything here. When they come up much later, use a cloud environment instead.</p>
    <p><strong>Don't try to run local AI models.</strong> With 8GB of unified memory at 60GB/s, anything you can fit will be too weak to be useful. Project 8 uses a hosted API. This is a limitation of the machine, not of you.</p>
    <p><strong>Browser discipline.</strong> Safari for reading and research, Chrome only when you're actively debugging a web page. Chrome with thirty tabs plus VS Code will push you into swap and everything will feel broken.</p>
    <p><strong>Extension discipline.</strong> Every VS Code extension costs memory. Install the four below and nothing else until something specific is genuinely annoying you.</p>
  </div>

  <p>If you have the 256GB model, keep an eye on disk space &mdash; the developer tools alone take a few gigabytes, and project folders accumulate faster than you'd think. Run <code>brew cleanup</code> occasionally and delete old virtual environments you're not using.</p>

  <h3>Before you install anything</h3>
  <p>Two macOS settings that will save you real confusion later:</p>
  <ul>
    <li><strong>Show file extensions.</strong> Finder &rarr; Settings &rarr; Advanced &rarr; tick "Show all filename extensions". Otherwise you can't tell <code>notes.txt</code> from <code>notes.py</code>.</li>
    <li><strong>Speed up key repeat.</strong> System Settings &rarr; Keyboard &rarr; drag Key Repeat Rate to fast and Delay Until Repeat to short. You'll be holding down arrow keys a lot.</li>
  </ul>
</section>

<section id="install">
  <div class="eyebrow">Setup</div>
  <h2>Installing everything</h2>
  <p>Open Terminal &mdash; press <code>&#8984; + Space</code>, type "Terminal", hit enter. Everything below gets typed in there. Type the commands out rather than pasting where you can; you'll remember them.</p>

  <h3>1 &mdash; Apple's developer tools</h3>
  <p>A one-off download that a lot of other things depend on. A window will pop up asking you to confirm. It takes a few minutes.</p>
  <div class="code"><button class="copy">Copy</button><pre><code>xcode-select --install</code></pre></div>

  <h3>2 &mdash; Homebrew</h3>
  <p>The package manager for macOS. It's how you install developer tools without hunting for download links. It'll ask for your password &mdash; that's normal, and it's the only time anything here will.</p>
  <div class="code"><button class="copy">Copy</button><pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre></div>
  <p>When it finishes it will tell you to run two more commands. Run these &mdash; on Apple Silicon, Homebrew installs to <code>/opt/homebrew</code> and your terminal needs telling where to find it:</p>
  <div class="code"><button class="copy">Copy</button><pre><code>echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' &gt;&gt; ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew --version</code></pre></div>
  <p>If that last line prints a version number, you're good. If it says "command not found", close Terminal completely and reopen it.</p>

  <h3>3 &mdash; Python</h3>
  <p>macOS ships with a Python, but it's there for the system's own use and you shouldn't build on it. Install your own:</p>
  <div class="code"><button class="copy">Copy</button><pre><code>brew install python
python3 --version</code></pre></div>

  <h3>4 &mdash; Git</h3>
  <p>Also pre-installed, also worth replacing with a current version:</p>
  <div class="code"><button class="copy">Copy</button><pre><code>brew install git
git --version</code></pre></div>

  <h3>5 &mdash; VS Code</h3>
  <div class="code"><button class="copy">Copy</button><pre><code>brew install --cask visual-studio-code</code></pre></div>
  <p>Open it, then press <code>&#8679;&#8984;P</code>, type "shell command", and pick <em>Install 'code' command in PATH</em>. Now you can type <code>code .</code> in any folder to open it.</p>
  <p>Install exactly these four extensions and stop:</p>
  <ul>
    <li><strong>Python</strong> (Microsoft) &mdash; the language support</li>
    <li><strong>Pylance</strong> &mdash; autocomplete and error highlighting</li>
    <li><strong>Ruff</strong> &mdash; catches mistakes and formats your code</li>
    <li><strong>GitLens</strong> &mdash; shows you the history of every line</li>
  </ul>

  <h3>6 &mdash; Terminal survival kit</h3>
  <p>You need about eight commands. Everything else you can look up.</p>
  <table>
    <tr><th>Command</th><th>What it does</th></tr>
    <tr><td><code>pwd</code></td><td>Where am I?</td></tr>
    <tr><td><code>ls</code></td><td>What's in here? (<code>ls -la</code> shows hidden files too)</td></tr>
    <tr><td><code>cd folder</code></td><td>Go into a folder. <code>cd ..</code> goes back up. <code>cd ~</code> goes home.</td></tr>
    <tr><td><code>mkdir name</code></td><td>Make a folder</td></tr>
    <tr><td><code>touch file.py</code></td><td>Make an empty file</td></tr>
    <tr><td><code>code .</code></td><td>Open this folder in VS Code</td></tr>
    <tr><td><code>python3 file.py</code></td><td>Run a Python file</td></tr>
    <tr><td><code>ctrl + c</code></td><td>Stop whatever is running. Your escape hatch.</td></tr>
  </table>
  <div class="note">
    <div class="lbl">Two habits worth forming now</div>
    <p>Press <strong>Tab</strong> to autocomplete file and folder names &mdash; it prevents typos and it's much faster. Press the <strong>up arrow</strong> to get your last command back rather than retyping it.</p>
  </div>
</section>

<section id="github">
  <div class="eyebrow">Setup</div>
  <h2>Git &amp; GitHub</h2>
  <p>Git tracks the history of your code on your machine. GitHub is where that history lives online. They're separate things and it's worth keeping them separate in your head.</p>

  <h3>Tell git who you are</h3>
  <p>Use the same email you'll use for GitHub, or your commits won't be linked to your account.</p>
  <div class="code"><button class="copy">Copy</button><pre><code>git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main</code></pre></div>

  <h3>Set up an SSH key</h3>
  <p>This lets you push code to GitHub without typing a password every time. Press enter at every prompt to accept the defaults.</p>
  <div class="code"><button class="copy">Copy</button><pre><code>ssh-keygen -t ed25519 -C "you@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
pbcopy &lt; ~/.ssh/id_ed25519.pub</code></pre></div>
  <p>That last command copied your public key to the clipboard. Go to GitHub &rarr; Settings &rarr; SSH and GPG keys &rarr; New SSH key, paste it in, and save. Then check it worked:</p>
  <div class="code"><button class="copy">Copy</button><pre><code>ssh -T git@github.com</code></pre></div>
  <p>It'll greet you by username. If it asks about authenticity the first time, type <code>yes</code>.</p>

  <div class="note warn">
    <div class="lbl">The one thing never to commit</div>
    <p>Passwords, API keys, tokens. Anything secret. Once it's in git history it's very hard to remove properly, and if it's been pushed publicly you have to assume it's compromised and rotate it. You'll set this up properly in project 3 &mdash; for now, just know it's a rule.</p>
  </div>
</section>

<section id="firstrepo">
  <div class="eyebrow">Setup</div>
  <h2>Your first repo</h2>
  <p>Do this now, before project 1. It's the loop you'll repeat for the next four months.</p>

  <div class="code"><button class="copy">Copy</button><pre><code><span class="c"># make a home for all your code</span>
mkdir -p ~/code &amp;&amp; cd ~/code

<span class="c"># make the project folder and go into it</span>
mkdir terminal-toolkit &amp;&amp; cd terminal-toolkit

<span class="c"># start tracking it with git</span>
git init

<span class="c"># make a virtual environment (keeps this project's</span>
<span class="c"># packages separate from every other project's)</span>
python3 -m venv .venv
source .venv/bin/activate

<span class="c"># open it in VS Code</span>
code .</code></pre></div>

  <p>Your terminal prompt now starts with <code>(.venv)</code> &mdash; that means the virtual environment is active. You need to run <code>source .venv/bin/activate</code> every time you come back to this project in a new terminal. Forgetting this is the single most common beginner confusion, and it usually shows up as "but I installed that package already".</p>

  <p>Create a file called <code>.gitignore</code> with this in it, so git ignores things that shouldn't be tracked:</p>
  <div class="code"><button class="copy">Copy</button><pre><code>.venv/
__pycache__/
.env
*.db
.DS_Store</code></pre></div>

  <h3>The commit loop</h3>
  <p>This is the rhythm. Every session, several times a session:</p>
  <div class="code"><button class="copy">Copy</button><pre><code>git status                          <span class="c"># what's changed?</span>
git add .                           <span class="c"># stage everything</span>
git commit -m "add dice roller"     <span class="c"># save a snapshot</span>
git push                            <span class="c"># send it to GitHub</span></code></pre></div>
  <p>The first time you push a new project, GitHub will give you a longer command to connect the folder to a repository. Make a new empty repo on GitHub, then copy what it tells you.</p>
  <p>Write commit messages as instructions: "add dice roller", "fix crash on empty input", "rename total function". Present tense, lowercase, says what changed. You'll be reading these back in four months.</p>
</section>

<section id="projects">
  <div class="eyebrow">Projects</div>
  <h2>Eight things to build</h2>
  <p class="lede">Each one takes two weeks and breaks in a way that teaches you the next thing.</p>
  <p>Every project has its own guide with six sessions, worked examples of each new idea, the traps that catch people, and a definition of done. Click through to start.</p>
  __SPINE__
  <h3 class="sec">Weeks 17&ndash;18: tidy up</h3>
  <p>Something will have slipped &mdash; it always does, and the buffer is deliberate. If nothing has, spend the time on presentation: proper READMEs with screenshots on all eight repos, a simple index page linking them together, and a pass through your commit history to see how far you've come.</p>
  <div class="note">
    <div class="lbl">What comes after this</div>
    <p>This guide covers August to November. If you're applying for a January bootcamp cohort, December is for the application itself &mdash; those have their own timed technical challenge with a different shape to project work, and it's worth a few weeks of specific practice. Different skill, different preparation. Ask your mentor to set that up nearer the time.</p>
  </div>
</section>

<section id="stuck">
  <div class="eyebrow">Reference</div>
  <h2>When you're stuck</h2>
  <p>Being stuck is the job. Not a sign you're failing at it. What matters is having a routine so that being stuck is boring rather than frightening. Work down this list in order.</p>
  <ol>
    <li><strong>Read the error properly.</strong> Actually read it. The last line says what went wrong; the line above it usually says where.</li>
    <li><strong>Fifteen minutes on your own.</strong> Set a timer. Change one thing at a time and see what happens.</li>
    <li><strong>Print things.</strong> Put <code>print()</code> before and after the broken bit. Is the variable what you think it is? It usually isn't.</li>
    <li><strong>Explain it out loud.</strong> To a colleague, a pet, an empty room. You'll solve it mid-sentence more often than you'd expect.</li>
    <li><strong>Search the exact error message.</strong> Paste it in, minus your own filenames and variable names.</li>
    <li><strong>Ask AI a question, not for the answer.</strong> See below.</li>
    <li><strong>Ask your mentor.</strong> Bring what you tried and what you expected, not just "it's broken".</li>
  </ol>
  <div class="note">
    <div class="lbl">Worth knowing</div>
    <p>Getting yourself unstuck is the single most valuable habit in this whole guide. Every time you push through step 4 instead of jumping to step 7, you're building the thing that actually makes someone employable.</p>
  </div>
</section>

<section id="git-ref">
  <div class="eyebrow">Reference</div>
  <h2>Git commands you'll actually use</h2>
  <table>
    <tr><th>Command</th><th>What it does</th></tr>
    <tr><td><code>git status</code></td><td>What's changed? Run this constantly.</td></tr>
    <tr><td><code>git add .</code></td><td>Stage all your changes</td></tr>
    <tr><td><code>git commit -m "msg"</code></td><td>Save a snapshot with a message</td></tr>
    <tr><td><code>git push</code></td><td>Send commits to GitHub</td></tr>
    <tr><td><code>git pull</code></td><td>Get changes from GitHub</td></tr>
    <tr><td><code>git log --oneline</code></td><td>See your history, one line each</td></tr>
    <tr><td><code>git diff</code></td><td>Show exactly what you changed</td></tr>
    <tr><td><code>git checkout -- file.py</code></td><td>Throw away changes to one file</td></tr>
    <tr><td><code>git branch feature-x</code></td><td>Make a branch</td></tr>
    <tr><td><code>git switch feature-x</code></td><td>Move to a branch</td></tr>
    <tr><td><code>git switch main</code></td><td>Go back to the main branch</td></tr>
    <tr><td><code>git merge feature-x</code></td><td>Bring a branch's work into this one</td></tr>
  </table>
  <div class="note warn">
    <div class="lbl">If git goes badly wrong</div>
    <p>Your work is almost never actually lost &mdash; git is very hard to destroy things with. Before trying anything drastic you found online, copy the whole project folder somewhere safe. Then you can experiment freely. Search "oh shit, git" for a short, practical guide to undoing common mistakes.</p>
  </div>
</section>

<section id="errors">
  <div class="eyebrow">Reference</div>
  <h2>Reading an error</h2>
  <p>Red text is not a punishment. It's the most useful information you'll get all day, and learning to read it is a real skill that most beginners avoid for far too long.</p>
  <div class="code"><pre><code>Traceback (most recent call last):
  File "tracker.py", line 42, in &lt;module&gt;
    total = add_up(expenses)
  File "tracker.py", line 18, in add_up
    return sum(e<span class="p">['amount']</span> for e in items)
KeyError: 'amount'</code></pre></div>
  <p>Read it from the <strong>bottom up</strong>:</p>
  <ul>
    <li><code>KeyError: 'amount'</code> &mdash; the actual problem. Something tried to get <code>'amount'</code> from a dictionary that doesn't have it.</li>
    <li><code>line 18, in add_up</code> &mdash; where it broke.</li>
    <li><code>line 42</code> &mdash; what called the thing that broke. Useful for working out how you got here.</li>
  </ul>
  <p>So: one of the expenses doesn't have an <code>amount</code> key. Probably one saved before you added that field. Now you know what to print out and check.</p>
  <h3>The four you'll meet most</h3>
  <table>
    <tr><th>Error</th><th>Usually means</th></tr>
    <tr><td><code>NameError</code></td><td>Typo in a variable name, or you used it before defining it</td></tr>
    <tr><td><code>TypeError</code></td><td>Wrong kind of thing &mdash; often a string where a number should be</td></tr>
    <tr><td><code>KeyError</code> / <code>IndexError</code></td><td>Asked for something that isn't in the dictionary or list</td></tr>
    <tr><td><code>IndentationError</code></td><td>Spacing is off. Python cares about indentation.</td></tr>
  </table>
</section>

<section id="readme">
  <div class="eyebrow">Reference</div>
  <h2>README template</h2>
  <p>Every repo gets one. Written for a stranger. This is not paperwork &mdash; explaining what you built is how you find out whether you understood it, and it's the first thing anyone looks at.</p>
  <div class="code"><button class="copy">Copy</button><pre><code># Project name

One sentence on what it does and who it's for.

## What it does
- Feature one
- Feature two

## Running it

    git clone git@github.com:you/project.git
    cd project
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 main.py

## What I learned
Two or three sentences. The bit that was hard, and how
you got past it. Write this for yourself in six months.

## What I'd do differently
Honest. Shows you can look at your own work critically.</code></pre></div>
  <p>Those last two sections matter more than they look. Anyone reading your GitHub can see that you can follow a tutorial &mdash; what they're looking for is evidence that you can think about your own work.</p>
</section>

<section id="ai">
  <div class="eyebrow">Reference</div>
  <h2>Using AI while you learn</h2>
  <p>You'll use AI every day as a working engineer. But there's a window &mdash; roughly the next four months &mdash; where leaning on it too hard stops you building the mental model that makes you useful. The distinction isn't whether you use it. It's what you ask for.</p>

  <div class="grid2">
    <div class="tile">
      <h4>Ask for this</h4>
      <p>"Why does this error happen?" &middot; "What does this line do?" &middot; "Ask me questions about my approach" &middot; "What edge case have I missed?" &middot; "Explain the difference between a list and a dictionary" &middot; "Review this and tell me what's unclear, but don't fix it"</p>
    </div>
    <div class="tile">
      <h4>Not this</h4>
      <p>"Write me an expense tracker" &middot; "Fix this for me" &middot; "Give me the code for user login" &middot; Anything where you'd paste the result in without being able to explain it afterwards.</p>
    </div>
  </div>

  <p>A useful framing: treat it as a tutor sitting next to you who has agreed not to write anything on your keyboard. It'll explain, question, and point out what you missed &mdash; but the typing is yours.</p>

  <div class="note">
    <div class="lbl">The test</div>
    <p>Can you explain every line you commit, unprompted, in six months? If yes, it doesn't matter how you got there. If no, you've skipped the part that mattered &mdash; go back and rebuild it yourself.</p>
  </div>
  <p>Once you're through project 8 and into professional work, open it all the way up. AI-assisted development is how the job is done now, and pretending otherwise would leave you behind. The restraint is temporary and it's for a reason.</p>
</section>

<section id="mentor">
  <div class="eyebrow">For the mentor</div>
  <h2>Running the sessions</h2>
  <p>The weekly loop matters more than the syllabus. Ninety minutes a week, same slot, is the highest-leverage thing available here &mdash; and it's the part that quietly dies around week five when work gets busy. Decide honestly now whether it's realistic.</p>

  <h3>The pairing session</h3>
  <ul>
    <li><strong>He drives, you navigate.</strong> He has the keyboard. You describe the destination, not the keystrokes. Swap for the last twenty minutes so he sees how you work.</li>
    <li><strong>Ask, don't tell.</strong> "What happens if that list is empty?" teaches; "you need a guard clause on line 12" doesn't. The gap between those two is most of the value you're adding.</li>
    <li><strong>Let the silence run.</strong> When he's thinking, wait. The urge to fill the gap with the answer is strong and worth resisting.</li>
    <li><strong>Make him read his own code aloud.</strong> Uncomfortable, and the fastest way to find the bits he doesn't actually understand.</li>
  </ul>

  <h3>Async review during the week</h3>
  <p>Look at his commits. Leave questions rather than corrections. Two or three per week is plenty &mdash; a wall of feedback on a beginner's first Flask app reads as a verdict rather than help.</p>
  <p>Things worth flagging early, because they compound: functions doing too many things, variable names that don't say what they hold, no error handling on anything touching the outside world, commit messages like "stuff" and "fixes".</p>

  <h3>What to watch for</h3>
  <div class="grid2">
    <div class="tile">
      <h4>Good signs</h4>
      <p>He arrives with specific questions. He can explain a bug before he can fix it. He goes back and improves old code unprompted. He's committing on days you didn't ask about.</p>
    </div>
    <div class="tile">
      <h4>Warning signs</h4>
      <p>Code appears that he can't walk you through. Commits stop for more than a week. He asks for the answer before describing what he tried. He's polishing project 1 in week 6.</p>
    </div>
  </div>

  <div class="note warn">
    <div class="lbl">The main failure mode</div>
    <p>Solving things for him. Every time you hand over an answer you save him twenty minutes and cost him the reflex the whole plan is trying to build. The programmes he's aiming at select for people who can get themselves unstuck &mdash; so being slightly less helpful than feels natural is, here, the more useful thing to be.</p>
  </div>
</section>
""".replace("__SPINE__", spine())
