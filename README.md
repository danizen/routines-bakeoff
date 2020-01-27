# routines-bakeoff

A simple app to test static site generation capabilities of Gatsby, Nuxt, and Django

## Data Model

A routine is a list of activities that are displayed as checkboxes each day

```javascript
{
   name: "Morning",
   description: "Getting up and out the door",
   items: [
     "Shower",
     "Get dressed",
     "Take pills",
     "Make coffee",
     "Make breakfast",
     "Eat breakfast",
     "Get badge",
  ]
}
```
## Application

The index page is a list of routines by name and description
Each routine also has a landing page
There is a sitemap listing all these pages

## Implementations

Each implementation is a sub-directory with its own `.gitignore`

* routines-nuxt - the app with nuxt
* routines-gatsby - the app with gatsby
* routines-django - the app with Django
