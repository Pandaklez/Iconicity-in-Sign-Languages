library(lingtypology)
# Lets create a dataframe with links to video
languages = c("Russian Sign Language", "French Sign Language", "American Sign Language",
              "British Sign Language", "Spanish Sign Language", "Italian Sign Language",
              "German Sign Language", "Polish Sign Language", "Polish Sign Language",
              "Brazilian Sign Language", "Turkish Sign Language", "Portuguese Sign Language",
              "Czech Sign Language", "Lithuanian Sign Language", "Swedish Sign Language",
              "Latvian Sign Language", "Estonian Sign Language", "Icelandic Sign Language")
popup = c("https://media.spreadthesign.com/video/mp4/12/14127.mp4",
          "https://media.spreadthesign.com/video/mp4/10/14126.mp4",
          "https://media.spreadthesign.com/video/mp4/13/124309.mp4",
          "https://media.spreadthesign.com/video/mp4/1/14132.mp4", 
          "https://media.spreadthesign.com/video/mp4/5/14130.mp4", 
          "https://media.spreadthesign.com/video/mp4/17/152515.mp4",
          "https://media.spreadthesign.com/video/mp4/9/14136.mp4",
          "https://media.spreadthesign.com/video/mp4/19/59919.mp4",
          "https://media.spreadthesign.com/video/mp4/19/59915.mp4",
          "https://media.spreadthesign.com/video/mp4/14/225758.mp4",
          "https://media.spreadthesign.com/video/mp4/11/14135.mp4", 
          "https://media.spreadthesign.com/video/mp4/6/14133.mp4",
          "https://media.spreadthesign.com/video/mp4/4/14129.mp4",
          "https://media.spreadthesign.com/video/mp4/3/14131.mp4",
          "https://media.spreadthesign.com/video/mp4/2/311877.mp4",
          "https://media.spreadthesign.com/video/mp4/26/60875.mp4",
          "https://media.spreadthesign.com/video/mp4/25/63019.mp4",
          "https://media.spreadthesign.com/video/mp4/21/52617.mp4")

patterns = c("object", "-", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "handling", "object", "object", "object")

sign_df <- data.frame(languages,
                      popup,
                      patterns)


# Change popup to an HTML code
sign_df$popup <- paste("<video width='200' height='150' controls> <source src='",
                       as.character(sign_df$popup),
                       "' type='video/mp4'></video>", sep = "")

View(sign_df)
# create a map
set.seed(3)
map.feature(languages = sign_df$languages,
            popup = sign_df$popup,
            minimap = TRUE)

