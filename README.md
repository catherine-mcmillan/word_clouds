# word_clouds
Basic scripts to create word clouds from TikTok comments for visual analysis

# Problem
Request from MSL Group Analytics SVP. MSL Analytics purchases tools that allow for the download of TikTok comments based on boolean queries. The comments can be downloaded into a CSV, but obtaining insights is a manual process. While LLM tools are capable of doing the text analysis to some degree, generating impactful easy to read and familiar visuals to include in high level infographics is more challenging. One common issue is the inclusion of common words relevant to the topic including brand names, product names, and query terms. 

The ASK was two-fold. 
1. Create an easy to use tool to parse TikTok comment exports into relevant phrases using n-grams weighted by frequency.
2. Create an easy to use and customizable a tool that creates word clouds with custom fonts, colors, and stop words.

# Solutions
 -- Efficiency first: The tool needed to make the team more efficient. This meant it needed to be accessible to people who had never used python and were unfamiliar with the command line. Additionally, the team needed effective training that could take them from 0 familiarity to competent daily user in under an hour. 

 -- Documentation: As a contractor, my time was valuable. The team wouldn't have access to me and my knowledge outside of our contract. The instructions and training needed to be strong enough that the team would be able to work without ongoing intervention from me. 

 # Results 
 -- The attached scripts formed the backing code used for the tools. The instructions provided are also available. Training for the SVP of Analytics and their team was done leveraging VSCode by request to minimize development time and encourage the team to become more familiar with homegrown technical solutions rather than costly market tools. Since that time, the Analytics team has begun offering the custom word clouds as a service offering that is completely done by the team to add visual references to reports leveraging TikTok comments. 
