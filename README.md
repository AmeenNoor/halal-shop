
# Halal Shop

# Author

Ameen Noor

# Introduction

Online Halal shop in Ireland, covering all regions of the country. Shop offers high-quality Halal-certified products, from fresh meats and groceries to household essentials. Browse the wide selection and enjoy the convenience of having authentic Halal items delivered to your door. Whether shopping for your family or stocking up on essentials, the shop provides a seamless and reliable shopping experience for all Halal needs.

![Am I Responsive](https://github.com/AmeenNoor/halal-shop/blob/main/readme/responsive/am-i-responsive.png)

Click [here](https://halal-shop-fb24ef103af0.herokuapp.com/) to visit the website.




# Table of Contents

- [Halal Shop](#halal-shop)
  - [Author](#author)
  - [Introduction](#Introduction)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [Target Audience](#target-audience)
  - [Goals](#goals)
  - [User Stories](#user-stories)
  - [Feasibility vs Importance](#feasibility-vs-importance)
  - [Scope](#scope)
  - [Design Choices](#design-choices)
  - [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
- [Agile Process](#agile-process)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Tools, Libraries and Programs Used](#frameworks-tools-libraries-and-programs-used)
- [Testing](#testing)
  - [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Validation Testing](#validation-testing)
  - [Manual Testing](#manual-testing)
  - [Defects](#defects)
- [E-commerce Business Model](#e-commerce-business-model)
  - [Facebook Business Page](#facebook-business-page)
  - [Newsletter Signup](#newsletter-signup)
  - [SEO Strategy](#seo-strategy)
- [Deployment](#deployment)
  - [Local deployment](#local-deployment)
  - [Heroku](#heroku)
- [Credits](#credits)
  - [Mentor](#mentor)


# UX
## Target Audience
- Muslims living in Ireland who want to buy Halal products easily.
- People who find shopping online convenient.
- Busy individuals, like workers and parents, who need a quick way to get groceries.
- Non-Muslims interested in trying Halal foods or products.
- Businesses, like restaurants or cafes, that need Halal ingredients for their dishes.

## Goals
**Customer Goals:**
- Easy Shopping: Make it easy for customers to find and buy halal products.
- Sorting Products: Help customers sort products by name or price to find what they want quickly.
- Cart Control: Let customers easily see what they've added to their cart and how much it costs.
- Smooth Checkout: Make it simple for customers to fill in their details and pay securely.
- Feeling Safe: Ensure customers feel safe buying from the website and know their information is protected.
- Quick Help: Provide fast help through email or phone if customers have questions or problems.

**Website Owner Goals:**
- Get Noticed: Make sure lots of people see the website, maybe by showing up well in search engines.
- Engage Customers: Encourage customers to share the website and products on social media.
- Manage Stock: Keep track of what products are in stock and update the website when things change.
- Grow Business: Find ways to sell more products and reach more customers.
- Make Money: Earn money through partnerships and ads to keep the website running.

**Overall Website Goals:**
- Happy Customers: Make sure customers are happy with their shopping experience.
- Work Efficiently: Make it easy for the business to manage everything behind the scenes.
- Earn Money: Find ways to make money while helping customers find what they need.
- Keep Improving: Always look for ways to make the website better based on feedback and new ideas.

## User Stories
### Site Visitor

- As a Site Visitor I can register for an account so that I can access additional features
- As a Site Visitor I can browse through a variety of products so that I can find items that interest me
- As a Site Visitor I can view detailed information about a product including images and descriptions so that I can make an informed purchasing decision
- As a Site Visitor I can search for products so that I can quickly find specific items of interest
- As a Site Visitor I can view products by category so that I can explore items within specific product categories
- As a Site Visitor I can filter products based on different criteria so that I can narrow down my product search
- As a Site Visitor I can add products to my cart so that I can keep track of items I intend to purchase
- As a Site Visitor I can edit products in my cart before proceeding to payment so that I can customize my order according to my preferences
- As a Site Visitor I can view the contents of my cart so that I can review the items I have added before proceeding to checkout
- As a Site Visitor I can preview the order summary before proceeding to checkout so that I can review the total costs and items in my cart
- As a Site Visitor I can proceed to checkout and complete my purchase so that I can finalize my order and make payment

### Registered User

- As a Registered User I can log in to my account so that I can access personalized content and manage my account
- As a Registered User I can log out of my account so that I can ensure secure access and protect my privacy
- As a Registered User I can change my account password so that I can maintain account security
- As a Registered User I can recover my account password if forgotten so that I can regain access to my account
- As a Registered User I can view my account details so that I can review my personal information and account settings
- As a Registered User I can fill out the checkout form with my shipping and payment details so that I can proceed with the purchase
- As a Registered User I can make payment for my order securely so that I can complete the purchase
- As a Registered User I can receive confirmation of my order so that I can have assurance that my order has been processed successfully

### Admin User

- As an Admin User I can add new products to the website so that I can expand the product catalog and offer more options to users
- As an Admin user I can edit existing products so that I can update product information and maintain accuracy
- As an Admin User I can remove products from the website so that I can manage the product catalog and remove outdated or discontinued items

## Feasibility vs Importance

To scope the project for an MVP (minimally viable product), a feasibility analysis was conducted.


| Opportunity/Feature                       | Feasibility/Viability (score out of 5) | Purpose Level of Importance (score out of 5) | In Or Out |
|-------------------------------------------|----------------------------------------|---------------------------------------------|-----------|
| Register for an account                   | 5                                      | 5                                           | In        |
| Browse through a variety of products      | 5                                      | 5                                           | In        |
| View detailed information about a product | 5                                      | 5                                           | In        |
| Search for products                       | 4                                      | 5                                           | In        |
| View products by category                 | 5                                      | 5                                           | In        |
| Filter products based on different criteria | 4                                      | 5                                           | In        |
| Add products to cart                      | 5                                      | 5                                           | In        |
| Edit products in cart                     | 5                                      | 4                                           | In        |
| View contents of cart                     | 5                                      | 5                                           | In        |
| Preview order summary                     | 5                                      | 5                                           | In        |
| Proceed to checkout and complete purchase | 4                                      | 5                                           | In        |
| Log in to account                         | 5                                      | 5                                           | In        |
| Log out of account                        | 5                                      | 5                                           | In        |
| Change account password                   | 5                                      | 5                                           | In        |
| Recover account password                  | 5                                      | 5                                           | In        |
| View account details                      | 5                                      | 4                                           | In        |
| Fill out checkout form                    | 5                                      | 5                                           | In        |
| Make payment for order securely           | 4                                      | 5                                           | In        |
| Receive confirmation of order             | 5                                      | 5                                           | In        |
| Add new products                          | 5                                      | 5                                           | In        |
| Edit existing products                    | 5                                      | 5                                           | In        |
| Remove products                           | 5                                      | 4                                           | In        |
| User Reviews and Ratings                  | 3                                      | 3                                           | OUT       |
| Wishlist Functionality                    | 3                                      | 3                                           | OUT       |
| Order Tracking                            | 3                                      | 4                                           | OUT       |
| Promotions and Discounts                  | 3                                      | 4                                           | OUT       |
| Multi-language Support                    | 2                                      | 2                                           | OUT       |

This table shows the importance features based on their feasibility and importance.

## Scope

To focus on creating a functional MVP, the scope has been narrowed to essential features only. Advanced functionalities and less critical features are excluded to ensure feasibility and maintainability. The goal is to implement basic, high-impact features.

- **In Scope:**
  - User registration and login
  - Browsing and viewing products
  - Adding products to cart
  - Viewing and editing cart contents
  - Basic product search and category view
  - Simple checkout process with order confirmation

- **Out of Scope:**
  - User Reviews and Ratings
  - Wishlist Functionality
  - Order Tracking
  - Promotions and Discounts
  - Multi-language Support

The approach ensures that the MVP is both achievable and provides value to users.



## Design Choices
- #### Colors
The chosen colors include blue, gray, white, and dark gray. Blue evokes a sense of safety, while gray adds a modern touch. White provides clarity, and dark gray offers contrast. Together, these colors aim to create a confident and comfortable user experience.

![colors](https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/design/colors.png)

- #### Typography
The 'Rye' font was chosen for the logo part to give a nice appearance and clear visual. 'Nanum Myeongjo' was selected for its readability, ensuring clear body text.
- #### Images
Chosen images display halal-certified products and halal food, showing that the items on the site are halal and good. Also, simple icons like the search and shopping cart symbols help users know what they can do, like searching or viewing their cart.
## Wireframes
- #### Desktop

<img src="https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/wireframes/desktop-home-page.png" alt="Desktop 1" width="270px" height="270px"> <img src="https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/wireframes/desktop-product-page.png" alt="Desktop 2" width="270px" height="270px"> <img src="https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/wireframes/desktop-product-detail-page.png" alt="Desktop 2" width="270px" height="270px">

- #### Mobile

<img src="https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/wireframes/mobile-home-page.png" alt="Desktop 1" width="200px"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/wireframes/mobile-product-page.png" alt="Desktop 2" width="200px"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://github.com/AmeenNoor/halal-shop/blob/main/readme/ux/wireframes/mobile-product-detail-page.png" alt="Desktop 2" width="200px">



# Information Architecture
## Entity Relationship Diagram

![Entity Relationship Diagram](https://github.com/AmeenNoor/halal-shop/blob/main/readme/data/output.png)

## Database Choice
PostgreSQL was chosen as the database for its relational data model. Additionally, Heroku provides PostgreSQL support out-of-the-box, making it easy to deploy and manage the application without incurring additional costs.

## Data Models

### Product Model

### Fields:
- `name`: CharField (max_length=250)
- `description`: TextField
- `price`: DecimalField (max_digits=10, decimal_places=2)
- `category`: CharField (max_length=250) with choices for different categories
- `image`: ImageField (optional, null=True, blank=True)

### Accessors:
- `get_name()`: Returns the name of the product.
- `get_description()`: Returns the description of the product.
- `get_price()`: Returns the price of the product.
- `get_category_display()`: Returns name of the category.
- `get_image_url()`: Returns the URL of the product image.

### Operations:
- **CREATE:** Handled by ProductCreate view.
- **READ:** Handled by ProductList and ProductDetail views.
- **UPDATE:** Handled by ProductUpdate view.
- **DELETE:** Handled by ProductDelete view.

## Order Model

### Fields:
- `user`: ForeignKey to User model (on_delete=models.CASCADE)
- `order_number`: CharField (max_length=32)
- `full_name`: CharField (max_length=50)
- `email`: EmailField (max_length=254)
- `phone_number`: CharField (max_length=20)
- `postcode`: CharField (max_length=20, optional)
- `town_or_city`: CharField (max_length=40)
- `street_address1`: CharField (max_length=80)
- `street_address2`: CharField (max_length=80, optional)
- `county`: CharField (max_length=80, optional)
- `date`: DateTimeField (auto_now_add=True)
- `delivery_fee`: DecimalField (max_digits=6, decimal_places=2)
- `subtotal`: DecimalField (max_digits=10, decimal_places=2)
- `total`: DecimalField (max_digits=10, decimal_places=2)

### Accessors:
- `get_order_number()`: Returns the order number.
- `get_full_name()`: Returns the full name of the customer.
- `get_email()`: Returns the email of the customer.
- `get_phone_number()`: Returns the phone number of the customer.
- `get_date()`: Returns the date of the order.
- `calculate_subtotal()`: Calculates the subtotal of the order.
- `calculate_total()`: Calculates the total of the order (subtotal + delivery_fee).

### Operations:
- **CREATE:** Handled by CheckoutView view.
- **READ:** Handled by OrderHistoryView view.

### OrderItem Model

### Fields:
- `order`: ForeignKey to Order model (related_name='items', on_delete=models.CASCADE)
- `product`: ForeignKey to Product model (on_delete=models.CASCADE)
- `quantity`: PositiveIntegerField (default=1)

### Accessors:
- `get_order()`: Returns the order to which the item belongs.
- `get_product()`: Returns the product associated with the item.
- `get_quantity()`: Returns the quantity of the product in the order item.

### Operations:
- **CREATE:** Handled when an order is created.
- **READ:** Accessed through the order's related items.


# Agile Process

Project follows an Agile development approach, focusing on iterative development and incremental improvements to deliver value to users in successive releases.

## User Stories
User stories are used to capture requirements and drive development. They are classified into four categories: **Must-Have**, **Should-Have**, **Could-Have**, and **Won't Have**.

## Epics
Epics represent high-level features of the project. Each epic consists of several user stories that collectively deliver the desired functionality.

### Epics Summary:
- **[EPIC:Project Setup and Configuration](https://github.com/AmeenNoor/halal-shop/issues/28)**
- **[EPIC: User Authentication and Account Management](https://github.com/AmeenNoor/halal-shop/issues/29)**
- **[EPIC: Product Management](https://github.com/AmeenNoor/halal-shop/issues/30)**
- **[EPIC: Product Catalog and Browsing ](https://github.com/AmeenNoor/halal-shop/issues/31)**
- **[EPIC: Shopping Cart and Checkout](https://github.com/AmeenNoor/halal-shop/issues/32)**

## Iterative Development
Development is organized into iterations, with each iteration focusing on specific features or functionalities. User stories are grouped into iterations based on their priority and dependencies.

### Iterations Summary:
- **[Iteration 0: Project Setup](https://github.com/AmeenNoor/halal-shop/milestone/2?closed=1)**
- **[Iteration 1: Product Browsing](https://github.com/AmeenNoor/halal-shop/milestone/3?closed=1)**
- **[Iteration 2: User Authentication](https://github.com/AmeenNoor/halal-shop/milestone/4?closed=1)**
- **[Iteration 3: Product Management](https://github.com/AmeenNoor/halal-shop/milestone/5)**
- **[Iteration 4: Shopping Cart](https://github.com/AmeenNoor/halal-shop/milestone/6?closed=1)**
- **[Iteration 5: Account Management](https://github.com/AmeenNoor/halal-shop/milestone/7?closed=1)**

# Features

## Implemented Features

1. **Responsive Design**
   - Webside is designed to be fully responsive, ensuring an optimal viewing experience across various devices, including desktops, tablets, and mobile phones.

2. **Navigation**
   - The header includes navigation links, providing easy access to different sections of the website.

3. **Product Listings**
   - The main content area displays a list of products, each represented as a card. Products include an image, name, price, and category for quick reference. Users can click on "More Details" to view additional information about each product.

4. **Cart Functionality**
   - Users can add products to their cart directly from the product listings or detail pages.

5. **Checkout Process**
   - Checkout process allows users to finalize their purchase. This includes filling out necessary information, reviewing the order summary, and making payments.

6. **User Authentication**
   - Users can create accounts, log in, and log out. Authentication is required for certain actions like adding products to the cart and checking out.

7. **Order Management**
   - Users can view their past orders and order details through their profile. Each order includes information such as order number, product details, subtotal, delivery fee, and total amount.

8. **Administrative Functions**
   - Admin users can create, update, and delete products through dedicated admin views.

9. **Error Handling**
    - Custom 404 and 500 error pages have been implemented to handle page-not-found and server errors.

## Future Features

1. **User Reviews and Ratings**
   - Allow users to leave reviews and ratings for products they have purchased.

2. **Wishlist Functionality**
   - Introduce a wishlist feature that allows users to save products they are interested in for future purchase.

3. **Order Tracking**
   - Provide users with the ability to track the status of their orders in real-time.

4. **Promotions and Discounts**
   - Introduce features for promotional codes and discounts, allowing users to apply special offers during checkout.

5. **Multi-language Support**
   - Implement multi-language support to cater to a wider audience, allowing users to navigate and use the website in their preferred language.




## Technologies Used
### Languages Used
1. HTML
2. CSS
3. Python
   
### Frameworks, Tools, Libraries and Programs Used
1. [Heroku](https://www.heroku.com/):
   Heroku was employed for project deployment.

2. [GitHub](https://github.com/):
   GitHub was utilized to store the project file and folder remotely.

3. [Git](https://git-scm.com/):
   Git was used in the Gitpod terminal to add, commit, and then push the changes to GitHub.

4. [CI's pep8 tool](https://pep8ci.herokuapp.com/):
   CI's pep8 tool was used to ensure the code is valid and follows proper indentation

5. [draw.io](https://app.diagrams.net/):
   draw.io was used to craft the flowchart

6. [Font Awesome](https://fontawesome.com/):
   Font Awesome was used to incorporate social media and contact information icons, including icons for Facebook, Twitter, Youtube, Instagram, email and address.
   
7. [Google Fonts](https://fonts.google.com/):
   Google fonts were used to import 'nanum myeongjo' & 'Rye' fonts into the style.css file which are used on all pages throughout the project.

8. [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/):
   Bootstrap was utilized for the styling and layout of the website.

9. [Jigsaw](https://jigsaw.w3.org/css-validator/):
   The CSS code of the website was tested using Jigsaw that provided by The World Wide Web Consortium (W3C).

10. [Jshint](https://jshint.com/):
   Jshint was used to validate javascript code.

11. [Balsamiq](https://balsamiq.com/):
   Balsamiq was used to create the mockup design for the website.

12. [Django](https://www.djangoproject.com/):
   Django was used to develop the backend, handling dynamic pages, URL routing, and database management.
        
13. [ElephantSQL](https://www.elephantsql.com/):
   ElephantSQL Was used to host the PostgreSQL database.

14. [w3c Markup Validator](https://validator.w3.org/):
   was used to validate code

15. [AWS S3 and IAM](https://eu-north-1.console.aws.amazon.com/console/home?region=eu-north-1) was used to host static and media files





# Testing
## Cross Browser and Cross Device Testing
The website was tested on various browsers and devices to ensure compatibility and optimal user experience. The testing process yielded successful results for most browsers and devices. See table and screenshots below:

<div align="center">

| Device                    | Browser         | OS       | Screen Width | Status |
| ------------------------- | --------------- | -------- | ------------ | ------ |
| dev tools: iPhone SE      | Chrome          | iOS      | 375 x 667    | ✔      |
| dev tools: iPhone 12      | Chrome          | iOS      | 390 x 844    | ✔      |
| dev tools: iPad Air       | Chrome          | iOS      | 820 x 1180   | ✔      |
| dev tools: Galaxy S8      | Chrome          | Android  | 362 x 740    | ✔      |
| real computer: Toshiba    | Microsoft Edge  | Windows 10 | 1366 x 768  | ✔      |
| real computer: Toshiba    | Firefox         | Ubuntu 22.04 | 1920 x 1080 | ✔      |
| real computer: MacBook Pro 13" | Safari    | iOS      | 1920 x 1080  |  ✔     |
| real mobile phone: iPhone 7 Plus | Safari    | iOS      | 1920 x 1080  |  ✔     |

</div>

## Accessibility Testing
Accessibility testing was done on the website, and Lighthouse, a testing tool, was used for this purpose. The Lighthouse report, displayed in the provided screenshot.

![CSS Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/accessibility/accessibility.png)

## Validation Testing
### CSS Validator
Validation testing was performed using Jigsaw to ensure code quality. Here is the validation testing results:

![CSS Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/css/css-test.png)

### HTML Validator
Validation testing was performed to ensure code quality. Here are the validation testing results:

- **Home Page**
![Home Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/home-error.png)

![Home Fixed](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/home-error-fixed.png)

- **Product Page**
![Product Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/product-error.png)

![Product Fixed](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/product-error-fixed.png)

- **Product Detail Page**
![Product Detail Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/product-detail-error.png)

![Product Detail Fixed](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/product-detail-error-fixed.png)

- **Cart Page**
![Cart Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/cart.png)

- **Checkout Page**
![Checkout Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/html/checkout.png)

### JS Validation
Validation testing was performed using JSHint to ensure code quality. Here are the validation testing results:

- **quantity input**
![Quantity Input Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/js/quantity-input.png)
- **stripe**
![Stripe Test](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/js/stripe.png)

### CI's pep8 tool
Validation testing was performed using CI's PEP8 tool to ensure code quality. Here are the validation testing results for each file:

#### halal-shop app:
- **views.py**
![Views](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/halal-shop-views.png) 
- **urls.py**
![URLS](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/halal-shop-urls.png)

#### home app:
- **views.py**
![Views](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/home-views.png) 
- **urls.py**
![URLS](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/home-urls.png)

#### products app:
- **views.py**
![Views](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/products-views.png) 
- **urls.py**
![URLS](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/products-urls.png)
- **models.py**
![Models](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/products-models.png)
- **forms.py**
![Forms](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/products-forms.png)

#### cart app:
- **views.py**
![Views](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/cart-views.png) 
- **urls.py**
![URLS](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/cart-urls.png)
- **contexts.py**
![Contexts](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/cart-contexts.png)

#### checkout app:
- **views.py**
![Views](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/checkout-views.png) 
- **urls.py**
![URLS](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/checkout-urls.png)
- **models.py**
![Models](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/checkout-models.png)
- **forms.py**
![Forms](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/checkout-forms.png)

#### profiles app:
- **views.py**
![Views](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/profiles-views.png) 
- **urls.py**
![URLS](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/profiles-urls.png)
- **models.py**
![Models](https://github.com/AmeenNoor/halal-shop/blob/main/readme/testing/validation_testing/python/profiles-models.png)

## Manual Testing


| Test ID | Test Title                         | Test Steps                                                                                 | Device (Browser-OS)                | Expected Outcome                                                                                             | Executed Date | Status |
|---------|------------------------------------|-------------------------------------------------------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------|---------------|--------|
| 001     | Register for an Account            | 1. Navigate to the registration page. <br> 2. Fill out the registration form with valid information. <br> 3. Submit the form. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Account is successfully registered; user receives a confirmation email if applicable.                     | 2024-07-04    | Pass   |
| 002     | Browse Products                    | 1. Navigate to the homepage or product listing page. <br> 2. Browse through different categories and products. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Products are displayed with images, descriptions, and prices; navigation is smooth.         | 2024-07-04    | Pass   |
| 003     | View Product Details               | 1. Click on a product from the product listing. <br> 2. View detailed information including images, descriptions, and specifications. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Product details are displayed accurately and completely; images are clear and informative.                  | 2024-07-04    | Pass   |
| 004     | Search for Products                | 1. Use the search bar to enter a specific product name or keyword. <br> 2. Press Enter or click on the search button. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Relevant search results are displayed matching the entered keywords or product name.                      | 2024-07-04    | Pass   |
| 005     | View Products by Category          | 1. Navigate to the product categories section. <br> 2. Click on a specific category to view products within that category. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Products within the selected category are displayed; category navigation is functional.                    | 2024-07-04    | Pass   |
| 006     | Filter Products                    | 1. Apply filters such as price range, name, or other criteria on the product listing page. <br> 2. View products that match the applied filters. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Products are filtered according to selected criteria; filters are applied correctly without errors.         | 2024-07-04    | Pass   |
| 007     | Add Products to Cart               | 1. Click on the "Add to Cart" button for a product. <br> 2. View the cart to confirm the product is added. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Product is successfully added to the cart; cart icon or indicator shows the updated quantity.              | 2024-07-04    | Pass   |
| 008     | Edit Products in Cart              | 1. Navigate to the cart page. <br> 2. Edit the quantity or remove products. <br> 3. Proceed to checkout. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Changes to the cart are reflected correctly; user can proceed to checkout with updated cart items. | 2024-07-04    | Pass   |
| 009     | View Cart Contents                 | 1. Click on the cart icon or link to view cart contents.                                    | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Cart page displays all added products with details like quantity, price, and subtotal.                      | 2024-07-04    | Pass   |
| 010     | Preview Order Summary              | 1. Proceed to checkout from the cart page. <br> 2. Review the order summary section.       | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Order summary displays accurate details including total costs and items in cart. | 2024-07-04    | Pass   |
| 011     | Proceed to Checkout                | 1. Click on the checkout button from the cart or order summary page. <br> 2. Fill out the required fields in the checkout form (shipping address, payment method, etc.). | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | User can progress through checkout without errors; form submission is successful.                          | 2024-07-04    | Pass   |
| 012     | Log In to Account                  | 1. Navigate to the login page. <br> 2. Enter valid credentials (username/email and password). <br> 3. Click on the login button. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | User is logged in successfully; access to personalized content and account management features is granted.  | 2024-07-04    | Pass   |
| 013     | Log Out of Account                 | 1. Click on the logout button or link.                                                     | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | User is logged out and redirected to the homepage or login page; session ends securely.                     | 2024-07-04    | Pass   |
| 014     | Change Account Password            | 1. Navigate to the account settings or profile page. <br> 2. Locate the password change section. <br> 3. Enter current password and new password; confirm new password. <br> 4. Save changes. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Password is updated successfully; user can log in with the new password.                                    | 2024-07-04    | Pass   |
| 015     | View Account Details               | 1. Access the account settings or profile page after logging in.                           | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | User's personal information and account settings are displayed accurately and securely.                    | 2024-07-04    | Pass   |
| 016     | Fill Out Checkout Form             | 1. Proceed to checkout after adding products to the cart. <br> 2. Fill out shipping and payment details in the checkout form. | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Form fields accept valid input; user can proceed with payment securely.                                     | 2024-07-04    | Pass   |
| 017     | Make Payment                       | 1. Choose a payment method and enter required details. <br> 2. Confirm payment.            | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Payment is processed successfully; user receives confirmation of the order.                                 | 2024-07-04    | Pass   |
| 018     | Receive Order Confirmation         | 1. After completing payment, check email or account dashboard.                             | Chrome-MacBook Pro 13.3 <br> Firefox-Ubuntu 22.04 | Confirmation email or message is received; order details are accurate and complete.                         | 2024-07-04    | Pass   |


## Defects
- **[Empty Cart Displays 'Proceed to Checkout' Button](https://github.com/AmeenNoor/halal-shop/issues/35)**
- **[Previous Messages Stay When New Notifications Show Up](https://github.com/AmeenNoor/halal-shop/issues/34)**
- **[Footer Position Fluctuates with Page Content](https://github.com/AmeenNoor/halal-shop/issues/33)**
- **[Sending Email Results in Error 500](https://github.com/AmeenNoor/halal-shop/issues/36)**

# E-commerce Business Model

The business model focuses on providing high-quality, halal-certified products to customers. Leveraging SEO strategies increases visibility and drives traffic to the site. Optimizing content with relevant keywords and meta tags aims to rank higher on search engines and attract more visitors.

## Facebook Business Page

![Facebook-1](https://github.com/AmeenNoor/halal-shop/blob/main/readme/facebook/facebook-1.png)

![Facebook-2](https://github.com/AmeenNoor/halal-shop/blob/main/readme/facebook/facebook-2.png)

![Facebook-3](https://github.com/AmeenNoor/halal-shop/blob/main/readme/facebook/facebook-3.png)

- **Goals:**
  - Build a strong community of followers.
  - Share special content and promotions exclusive to our Facebook followers.

- **Link:** [Halal Shop Facebook Page](https://www.facebook.com/profile.php?id=61560090561110)

## Newsletter Signup

![Newsletter](https://github.com/AmeenNoor/halal-shop/blob/main/readme/facebook/newsletter.png)

- **Goals:**
  - **Build Email Subscriber Base:** Increase the number of subscribers to our newsletter, allowing direct communication with interested customers.
  - **Customer Relationships:** Provide exclusive updates, promotions, and content directly to subscribers.

## SEO Strategy

- **Keywords:** Short-tailed and long-tailed keywords were identified through research and analysis, aligning with user search intent for halal products.

- **Description:** Meta description tags are used on each page, ensuring relevance and dynamic updates based on page content.

- **Title:** Dynamic title tags in the `base.html` template can be customized for each page to enhance SEO.

- **Sitemap:** The `sitemap.xml` file lists all site pages, facilitating easy crawling by search engines.

- **Robots.txt:** The `robots.txt` file restricts search engines from indexing certain pages, such as authentication pages, ensuring only relevant content is searchable.


# Deployment
## Local deployment
To deploy the site using Visual Studio Code, follow these steps:

1. **Clone the Repository:**
    * Open VS Code.
    * Use the command palette and run "Git: Clone".
    * Enter the GitHub repository URL and choose a local directory.
    * Open the cloned project in VS Code.

2. **Install Dependencies:**
    * Navigate to the project directory in the terminal & run the following:
    **pip3 install -r requirements.txt**

3. **Set Environment Variables:**
    * Create a .env file in the project root.
    * Copy the contents of env.py into the .env file.

4. **Apply Migrations:**
    * Run the following commands to apply migrations:
    **python3 manage.py migrate**

5. **Create Superuser :**
    * Create an admin superuser for accessing the Django admin panel:
    **python3 manage.py createsuperuser**

6. **Run the Server:**
    * Start the Django server:
    **python3 manage.py runserver**

## Heroku
To deploy the site on Heroku, follow these steps:

1. Begin by forking the repository: <https://github.com/AmeenNoor/halal-shop>.

2. Log in to Heroku and click "New." Select "Create new app."(see screenshots below):

![Deployment_1](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image1.png)

3. Choose a unique name for your app, select your desired region, and then click "Create app." (see screenshot below):

![Deployment_2](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image2.png)

1. In the app settings, navigate to the "Config Vars" section. Set the environment variables directly on Heroku (see screenshots below):

![Deployment_3](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image3.png)

![Deployment_4](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image4.png)

![Deployment_5](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image5.png)

1. Under the "Buildpacks" section, click "Add buildpacks." Add "python" as buildpacks. Ensure that Python is selected first, followed by Node.js. Save your selections. (see screenshots below):

![Deployment_6](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image6.png)

![Deployment_7](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image7.png)

1. In the "Deploy" section, choose "GitHub/Connect to GitHub" as your deployment method. Search for the project on GitHub and connect it. (see screenshots below):

![Deployment_8](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image8.png)

![Deployment_9](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image9.png)

![Deployment_10](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image10.png)

1. Finally, click "Deploy Branch" to deploy your project. (see screenshot below):

![Deployment_11](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image11.png)


# Credits
- The GitHub repository was created using the "Code Institute template." You can find the template at: [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template).

- The concepts for toast notifications, 404 & 500 error pages, Allauth integration, and the profile app were adopted from the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1).

- The carousel/slideshow code in use has been adapted by [W3Schools](https://www.w3schools.com/bootstrap5/tryit.asp?filename=trybs_carousel2).
   
- The responsive image is generated using the [Am I Responsive](https://ui.dev/amiresponsive) tool.
   
- The color scheme image is sourced from [Coolors](https://coolors.co/).

- The social media icons are sourced from [FontAwesome](https://fontawesome.com/).

- The fonts 'Rye' and 'Nanum Myeongjo' are sourced from [Google Fonts](https://fonts.google.com/).
   
- Website images are sourced from [Unsplash](https://unsplash.com/)
   
## Mentor
Huge thanks to my mentor **"Malia Havlicek"** for her support and guidance.

