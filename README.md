# CS 340 – Client/Server Development

## Grazioso Salvare Animal Rescue Dashboard

**Brian Minor**  
Southern New Hampshire University  
CS 340 – Client/Server Development

### Project Overview

For this project, I developed an interactive dashboard for Grazioso Salvare using Python, MongoDB, Dash, and Plotly. The purpose of the dashboard was to help the organization search and filter animal shelter records to identify dogs that could be candidates for rescue training.

The project involved creating a Python CRUD module to communicate with MongoDB and connecting that module to a dashboard with an interactive data table, filtering options, and a geolocation map.

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

When writing programs, I try to keep my code organized so it is easy to understand, troubleshoot, and update later. One of the biggest things I learned in this course was the importance of separating different parts of a program instead of putting everything into one file.

For Project One, I created a Python CRUD module that handled communication with the MongoDB database. When I started Project Two, I was able to reuse that same module to connect my dashboard to the animal shelter records. This made the project easier to manage because I didn't have to rewrite the database connection and query logic every time I needed information.

Another advantage was that I could make changes to the database code without having to completely change the dashboard. In the future, I could use a similar CRUD module for inventory management, employee records, or other applications that need to store and retrieve information from a database.

### How do you approach a problem as a computer scientist?

My approach to solving problems usually starts with understanding what the program needs to accomplish before jumping into writing code. For the Grazioso Salvare project, I looked at the requirements and broke them down into smaller tasks, such as importing the shelter data, creating database queries, building the CRUD module, and connecting everything to the dashboard.

This project was different from some of my previous assignments because I wasn't just writing code to demonstrate one concept. I had to make several technologies work together to create something that could actually be useful to an organization. There were times when I had to troubleshoot database connections, authentication issues, and dashboard functionality before everything worked correctly.

I found that testing each part individually made it easier to identify problems. Instead of trying to fix everything at once, I could narrow down where something wasn't working and make adjustments. Moving forward, I would continue using this approach while also spending more time planning database structures, understanding client requirements, and testing queries before building the rest of an application.

### What do computer scientists do, and why does it matter?

Computer scientists use technology and problem-solving skills to develop systems that make tasks easier, improve efficiency, and help organizations manage information. Their work goes beyond writing code because they also have to understand how people will use the software and what problems it is supposed to solve.

The Grazioso Salvare dashboard is a good example of this. Instead of having someone manually search through thousands of animal shelter records, the dashboard allows users to filter information and view results in a more organized way. The interactive table and geolocation map make it easier to identify animals that meet specific rescue training requirements.

For an organization like Grazioso Salvare, having this information readily available could save time and help staff make better decisions. This project helped me understand how database development and software design can work together to solve real-world problems. It also gave me more experience building applications that are useful beyond the classroom.
