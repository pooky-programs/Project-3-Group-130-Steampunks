COP3530 Project 3 README
Steampunks

---

Current Team Members:

  Joel Liston
  
  Serafina Myers
  
---

Previous Team Members:

  Austin Rhee
  
  Serafina Myers
  
  Jonathan Kennel

---

The aim of this project will be to provide game publishers or developers with information regarding current trends. This allows for informed decision making regarding game planning, and allows one to observe trends in genre popularity, prices, and other sets of information as it relates to average user reviews.

To run the project, use the CMakeLists.txt configuration file, and run main. Make sure that final_data.csv is in the data folder before you start, as this is the dataset our application uses.

---

References:

  SteamSpy API
  
    https://steamspy.com/api.php
  
  Official Steam Web API
  
    https://steamcommunity.com/dev 


  ---
  Tracked Data Points:

    Appid - Unique identifier for each item.
    Genre - Top describing the genre of the application.
    Type - Used to identify type of app. Includes games, demos, movies, and dlc.
    Owners - Roughly correlated with purchases, can be swayed by price, giveaways & discount frequency.
    Metacritic - Metacritic score for the app.
    Developers - Lead Developer
    Price - How much the game costs. Based on initial value, not the price when affected by steam sales.
    Positive - Positive reviews left by users.
    Negative - Negative reviews left by users.
    ccu - Concurrent users.
