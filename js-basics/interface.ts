interface Product{

    pdtFullName: string;
    
    toNumber();

    id: string;   
    name: string;   
    price: string;  
    description: string;  
    
    }
 

    
    interface Pricing {
    
    }
    
    interface cart extends Product, Pricing {
    
    }
    
    
    class Cosmetic{
    
    uId: string;
    
    cName: string;
    
    constructor (id: string, name: string) {
    
    this.uId= id;
    
    this.cName= name;
    
    }
    
    toString() {
    
    console.log(`cosmetic ID of ${this.cName}: ${this.uId}`);
    
    }
    
    }
    
    class Electronic{
    
    id: string;
    
    eName: string;
    
    constructor (id: string, name: string) {
    
    this.id= id;
    
    this.eName= name;
    
    }
    
    toString() {
    
    console.log(`EMP ID of ${this.eName}: ${this.id}`);
    
    }
    
    }
    
    
    // Instantiate both classes-

let cosmetic = new Cosmetic("2432423SR", "XYZ");

let electronic = new Electronic("SM43432", "");
 
// example Record

export const SERVICES: Record<string, string> = {  
    doorToDoor: "delivery at door",  
    airDelivery: "flying in", 
    specialDelivery: "special delivery",  
    inStore: "in-store pickup",  
  };  

  export class CartModel {  
  products: Record<string, ProductInCart>  
  errors ?: CartErrors; 
  }  

  export interface ProductInCart { 
  id: string;  
  amount: number;  
  name: string;  
  label ?: string;  
  }  

  export enum ErrorsEnum {  
  NetworkError = 'NetworkError',  
  ServerError = 'ServerError',  
  FormValidationError = 'FormValidationError',  
  UnknownError = 'UnknownError'  
  }  



  export interface Product4 {  
  id: string;  
  name: string;  
  price: string;  
  description: string;  
  author: string;   
  authorLink: string; 
  }  

  // example partial
  export type ModelProps = Partial<{ 
    product: Product;   
    cartContent: Record<string, ProductInCart>;  
    }>;  
  
    export type CartErrors =   
    Partial<Record<ErrorsEnum, string>>;  
    
    // example Required
    export type OwnProps = Required<{   
    name: string;  
    description: string;   
    ingredients: Array<Product>;   
    }>;  

    // example pick
  export type Product2  = Pick< Product4, 'id' | 'author' | 'authorLink' | 'price'>;  

  // example Omit
  export type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;  
  export type Product3 = Omit<Product4, 'name' | 'description'>;  
  