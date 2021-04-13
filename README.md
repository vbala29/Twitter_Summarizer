# NETS213 Final Project - Crowdsourced Hashtag Summarizer

**Component 1: Selecting top-trending hashtags from Twitter’s trending page that have been active for more than 24 hrs.** *(2 points)*

	For this component, we planned to select 10 hashtags from the Twitter trending page. We used newly created twitter accounts, that weren’t following anything, to view the trending page on Twitter, as we did not want accounts we followed to affect what we saw on the trending page. However, it was inevitable that our location affected what we saw on the trending page, which was okay, as we were more inclined to select English hashtags in general, rather than ones with tweets primarily in other languages. Note that Twitter states on their website that, “Trends are determined by an algorithm and, by default, are tailored for you based on who you follow, your interests, and your location.” Thus, it is possible that Twitter has collected data from sources besides just one’s location and what they follow on Twitter; thus, it may be impossible for us to truly see a generic Twitter trending page. We thought about using online data sites to track trending hashtags, but realized that the point of this project is not to select the top trending hashtags, but to simply select trending ones that may be obscure or unfamiliar to people, and thus require some sort of summary. 

We came up with selection criteria when choosing our 10 hashtags. Note that the hashtags are being chosen over a period of about 3 weeks (~3 hashtags per week), in order to create a timeline at the end of our project that displays crowdsourced summaries along with hashtags that were trending at points in our projects. The criteria we came up with was as follows. 1. Select hashtags that have been trending for more than 24 hrs. Once we spot a trending hashtag, we may check tweets in the hashtag to see if it has been very active for more than 24 hrs, or simply look up the news associated with that hashtag (example #Myanmar, related to the military coup in the country) and see how long ago the news came out.  2. Select hashtags with primarily English tweets. 3. Select hashtags that aren’t obvious as to what they are about. For example, #Biden2020 would be a bit too obvious as almost everyone knows what such a hashtag would be about. However, #dogecoin is not as obvious to many people, especially those not involved in cryptocurrency, finance, or part of gen-z. Selecting these types of hashtags makes the summarizing process more interesting, as we want to see varying results based on how much information/context (more/less/no tweets) we provide to workers to write their summaries.

**Component 2: Online-bot tweet-to-CSV service: provides a file with ~700 tweets, specifically ones associated to a given hashtag and with a minimum of 100 likes.** *(2 points)*
	
	We used the following Twitter bot to extract tweets from the hashtags that we had selected: https://seobots.io/bots/twitter-hashtag-scraper. This bot was cheap to use, and gave us the option to determine the number of tweets we wanted to scrape for in each hashtag, the language that the tweet needed to be in, and the minimum number of likes that a tweet needed to have. We selected a minimum of 100 likes so as to make sure that the tweets we were getting were representative of what most people interacting with the hashtag were actually interacting with. If we had set this barrier to zero, it is possible that we scraped tweets that were just “noise”—spam, or unrelated to the hashtag itself. This bot runs with a completion time of under two minutes. We noticed that on average, the bot was only able to parse about 600-800 tweets from each hashtag, possibly because of the filters we had set, as well a limit on how far back the bot could search. Thus, if a csv generated had less than 700 tweets, we would simply run the bot again the next day, and then merge the two csv generated to get a file with at least 700 tweets pertaining to that hashtag. It’s worth noting that the csv generated from this bot has columns for the following data: Username, User Handle, Date of Posting, Tweet Text, ReTweet Count, Like Count.

**Component 3: Generation 1 of HITs to generate summaries via crowdsourcing about why a particular hashtag is trending. Three different batches of HITs per hashtag for varying sources of information given to workers** *(4 points)*

**Component 4a: Generation 2 of HITs to use crowdsourcing as quality control, where three workers workers give ratings to each summary, allowing for averaged ratings to be generated** *(4 points)*

**Component 4b: Generation 2 of HITs using Twitter generated summaries about some of the hashtags (only one per hashtag). Yet again multiple workers will give ratings to each of these summaries and averaged ratings will be generated** *(2 points)*

**Component 5: Aggregation Module where various graphs comparing ratings in our 4 different categories (Google News, 10 tweets, 20 tweets, Twitter generated) of summaries will be generated.** *(3 points)*

GRAP ABOUT likes vs quality generated

**Component 6: Aggregation Module Part 2, where the best summaries are selected from each hashtag based on ratings from workers.** *(1 point)*

Point Total: 18 points
