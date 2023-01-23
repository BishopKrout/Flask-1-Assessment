### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 
Python is used for server side, data analysis. Large and extensive standard library. JavaScript is used for client-side scripting and creating interactive front-end web apps.
Python uses indentation to indicate code blocks, while JS uses curly braces. 
Python's syntax is consistent and simple, while JS's is more flexible and complex.
Python is synchronous and JS is asynchronous.
Python is used in Sci and Math often and JS is strictly web dev. 
Python is superior for data science and machine learning, JS is better front-end web dev.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  First option is to use the `get()` method of the dictionary. This method returns the value associated with the given key. Returns set default value if key is not found.
  Second option use the `in` operator to check if the key is in the dictionary before trying to access it. Example: `if "c" in "d": x = d["c"]`. Will check if key "c" is in dict of 'd'

- What is a unit test?

Unit testing is a method of testing individual units or components of a software app to ensure they work as intended. It is automated and written by devs, it is run every time code changes to catch bugs early. Test-driven development (TDD). 

- What is an integration test?

It is a method of verifying the interactions and connections between different components in a system, to ensure they work together properly. Happens after unit testing and before acceptance testing. 

- What is the role of web application framework, like Flask?

They provide a set of tools and libraries to simplify the development of web apps. They handle low-level web dev details and allow devs to focus on logic. Flask is lightweight and easy, it's used for small to medium projects

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  If the structure of the URL is important for readability purposes, then route parameters are a better fit. If the info being passed is secure or private, then query parameter better due to it being less exposed. Query parameter is also a better choice is caching is important because it is more flexible. 

- How do you collect data from a URL placeholder parameter using Flask?

You can use the `request` object and the `args` attribute. 

- How do you collect data from the query string using Flask?

Using the `request.args` attribute. It is dict-like and allows access to key-value pairs in the q-string. `request.args.get('key')` can be used to collect a specific query parameter and `request.args.getlist()` can be used for all values. Only works for GET requests. 

- How do you collect data from the body of the request using Flask?

By using the `request` object and its `data` or `json` attr. Is used when data is passed as arg in a submit func. `request.json` only works when content-type is set to `application/json`, for other types use `request.data`. Works for POST requests.   

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a small piece of data stored on a user's computer by a website, which can also be retrieved by the website. Commonly used for session managment, user preferences, and tracking behavior.

- What is the session object in Flask?

It's an easy way to store data on a per-session basis. The data is specific to each user and usable accross mulitple reqs. Implemented as a dict-like obj backed by secure cookie. A secret key is required to use it, set the key by `app.config['SECRET_KEY']` then use it to store data. 

- What does Flask's `jsonify()` do?

It is a function provided by Flask that allows you to convert python objects into JSON format and return them as the repsonse to an HTTP req, it also sets appropriate content type ("application/json") for the response, It is similar to `json.dumps()` but also handles other details, like JSON indentation, It returns a `Response` obj, which can be modified.
