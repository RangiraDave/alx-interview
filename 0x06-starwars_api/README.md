# Star Wars Characters

The "0. Star Wars Characters" project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

## Concepts Needed

- HTTP Requests in JavaScript:
    - Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
    - [A Complete Guide to Making HTTP Requests in Node.js](https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html)

- Working with APIs:
    - Understanding the basics of RESTful APIs and how to interact with them.
    - Parsing JSON data returned by APIs.
    - [Working with APIs in JavaScript](https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/)

- Asynchronous Programming:
    - Managing asynchronous operations with callbacks, promises, and async/await syntax.
    - Handling API response data asynchronously.
    - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

- Command Line Arguments in Node.js:
    - Using the `process.argv` array to access command-line arguments passed to a Node.js script.
    - [How to Parse Command Line Arguments in Node.js](https://www.digitalocean.com/community/tutorials/nodejs-command-line-arguments-node-scripts)

- Array Manipulation and Iteration:
    - Iterating over arrays and manipulating data structures to format and display character names.
    - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.

## Additional Resources
- [Mock Technical Interview](https://www.interviewing.io/recordings/)



## Tasks
0. Star Wars Characters
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
-  Display one character name per line <em>in the same order as the “characters” list in the ``/films/`` endpoint</em>
- You must use the [Star wars API](https://swapi-api.alx-tools.com/)
- You must use the ``request`` module
```
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 
```

## HappyCoding!
