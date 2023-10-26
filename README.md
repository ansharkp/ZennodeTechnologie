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

# ExoCarToken Project Plan

## Project Overview

The "ExoCarToken" project aims to create a decentralized application (DApp) for tracking and verifying the ownership of exotic cars using blockchain technology. This project involves smart contract development, user interaction, file storage, and transaction management.

## Steps for ExoCarToken

### Smart Contract Development:

1. **Design and Develop Smart Contracts:**
   - Design the smart contracts for ExoCarToken, following the ERC-721 standard for non-fungible tokens (NFTs).
   - Develop the smart contracts to include functions for adding file hashes, associating them with exotic cars, and managing ownership.

2. **Compile Smart Contracts Using Truffle:**
   - Use the Truffle development framework to compile your smart contracts. Truffle provides a development environment and tools for Ethereum smart contract development.

3. **Migrate Smart Contracts to Ganache:**
   - Deploy and migrate your smart contracts to the Ganache blockchain, which serves as your local development environment for testing.

### User Interaction:

4. **Users Connect Using MetaMask and Web3:**
   - Instruct users to connect to the Ganache blockchain using the MetaMask browser extension and Web3.js library. MetaMask allows them to interact with the DApp in their web browser.

5. **Run the ExoCarToken App:**
   - Develop the ExoCarToken app using React.js to provide a user-friendly interface for uploading files and interacting with the smart contract.

6. **Upload Files and Connect the App with Ganache:**
   - Users can upload files through the app, and the app should be connected to the Ganache blockchain to interact with the smart contract.

### File Storage and Retrieval:

7. **Publish Files to IPFS:**
   - Publish the uploaded files to IPFS, a decentralized and distributed file storage system.

8. **Retrieve File Hash from IPFS:**
   - Retrieve the unique file hash from IPFS for each uploaded file and return it to the app.

### Token Management:

9. **Add File Hash to Smart Contract:**
   - Users can associate the file hash with the ownership of a specific exotic car by adding it to the ExoCarToken smart contract.

### Transaction Approval:

10. **Users Approve Transactions Using MetaMask:**
    - Users need to approve the transaction using MetaMask to confirm the addition of the file hash to the smart contract. This step ensures the security and integrity of the data.

### Record User Interaction:

11. **Add File Hash and User Address to Smart Contract:**
    - Record the file hash and user's Ethereum address in the ExoCarToken smart contract to keep a transparent record of user interactions.

### View/Download File:

12. **View/Download Files:**
    - Users can view and download files associated with their exotic cars by interacting with the smart contract. The file hash helps retrieve the corresponding files from IPFS.

## Project Diagram

```mermaid
graph TD
    A[User] --> B[MetaMask: Connect]
    B --> C[ExoCarToken App: Run App]
    C --> D[Ganache: Connect]
    C --> E[Upload Files]
    E --> F[IPFS: Publish File to IPFS]
    E --> G[Return File Hash]
    G --> H[ExoCarToken App: View/Download Files]
    G --> I[Token Management]
    I --> J[Truffle: Compile Smart Contracts]
    I --> K[Ganache: Migrate Smart Contracts]
    I --> L[ExoCarToken App: Add File Hash]
    L --> M[MetaMask: Transaction Approval]
    L --> N[ExoCarToken App: Record User Interaction]

