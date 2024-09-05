# princeton-py-ai
Exploring how Copilot, ChatGPT, and Gemini can help us code.

## One-Off Tests

bad_loop.py is just a simple program I wrote with a while loop so I could ask the assistants how to improve it.

i_like_to_wait.py is another simple program where I tried to do matrix math but decided to be a little silly and did it in a for loop and asked the program to wait so the computer wouldn't overheat or get mad at me.

web_scrape_lpga_gemini.py was from an attempt I made to ask the assistants to generate code to determine what the next LPGA tournament was. ChatGPT and Copilot went the API route, so I decided to work with Gemini's attempt and did not need to edit too many lines of code to get it working (even if it's buggy and not particularly reliable!).

## Goofy Obstacle Course

I wrote a simple simulator (with minimal AI help) that would simulate three people running an imaginary obstacle course. The key elements were:

- A rope swing which could fail, and the competitor would have to redo until successful
- A wall climb which had 10 grips, each of which could be completed slowly or quickly (simulating stamina and randomness)
- A door challenge, where 5 levels of 5 doors exist but only 2 doors at each level can actually open

I then tried to explain this course to each of my AI assistants and their results are tagged appropriately.

## Web Scraper Birth Year

This is a more ephemeral problem, but I figured I'd give it a shot. In particular, I'm interested in how creative the default solution was at trying to look a person's birth year on their personal website. None of the solutions were particularly great.

## Other Random Resources

I've found this guide on different ways to prompt assistants very useful: https://www.promptingguide.ai/


