### Convert Rate Tag into Comment

As mentioned in the full guide, to make the Python script with plexx to work,the ratings from Swinsian needs to be converted into comment tags.

![MP3tag Tag to Tag](../img/mp3tag-tag-to-tags.png)

1. **Set Comment Tag** 
The following formula converts the rate tag to the comment tag:

 **Format tag field** 
Field: `COMMENT`
```text
%RATE%
```