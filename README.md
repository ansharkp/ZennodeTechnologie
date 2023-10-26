# ZennodeTechnologie
Python code for given question

Here is a catalog with 3 products.

Product Name	Price
Product A	$20
Product B	$40
Product C	$50
Discount Rules:

"flat_10_discount": If cart total exceeds $200, apply a flat $10 discount on the cart total.
"bulk_5_discount": If quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
"bulk_10_discount": If total quantity exceeds 20 units, apply a 10% discount on the cart total.
"tiered_50_discount": If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantity have the original price and unit above 15 will get 50% discount.
Note: Only one rule can be applied per purchase. If multiple discounts are applicable, the program calculates the discount amount for each rule and applies the most beneficial one for customer.

Fees:

Gift wrap fee: $1 per unit.
Shipping fee: 10 units can be packed in one package, and the shipping fee for each package is $5.
Program

The program will ask the quantity of each product. Same time, program will ask is that product is wrapped as gift?

Then the program will show / output below details.

The product name, quantity & total amount of that product.
Subtotal
The discount name applied & the discount amount.
The shipping fee & the gift wrap fee.
Total

graph TD
    A[Smart Contract Development] --> B[Design and Develop Smart Contracts]
    B --> C[Compile Smart Contracts Using Truffle]
    C --> D[Migrate Smart Contracts to Ganache]
    
    E[User Interaction] --> F[Users Connect Using MetaMask and Web3]
    F --> G[Run the ExoCarToken App]
    G --> H[Upload Files and Connect the App with Ganache]
    
    I[File Storage and Retrieval] --> J[Publish Files to IPFS]
    J --> K[Retrieve File Hash from IPFS]
    
    L[Token Management] --> M[Add File Hash to Smart Contract]
    
    N[Transaction Approval] --> O[Users Approve Transactions Using MetaMask]
    
    P[Record User Interaction] --> Q[Add File Hash and User Address to Smart Contract]
    
    R[View/Download File] --> S[View/Download Files]

