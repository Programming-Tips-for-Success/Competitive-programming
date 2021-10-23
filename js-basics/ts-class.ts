 class QuoteModel { 

    constructor(public text: String, public timeCreated: String) {} 
    
    }   
    
     class AppComponent {
    
    public quoteList: QuoteModel[] = []; 
    
    private daysOfTheWeeks = ["Sun", "Mon", "Tue", "Wed", "Thurs", "Fri", "Sat"]; 
    
      addNewQuote(quote: String) { 
    
      const date = new Date(); 
    
      const dayOfTheWeek = this.daysOfTheWeeks[date.getDate()]; 
    
      const day = date.getDay(); 
    
      const year = date.getFullYear(); 
    
      this.quoteList.push( 
    
        new QuoteModel(quote, `${dayOfTheWeek} ${day}, ${year}`) 
    
      ); // to create objects we can use QuoteModel class
    
        console.log(this.quoteList); 
    
    } 
    
      constructor(){
    
      console.log(this.addNewQuote('Motivational')); // {text: "Motivational", timeCreated: "Sat 4, 2020" }
    
    }
    
    }
    


    class User {

      username = '';
      tags = [];
      followers = [];

      /**
      * @param {string} username
      @param {Array.<string>} tags
      ***/
      constructor(username, tags) {
      this.username = username;
      this.tags = tags;
      this.followers = [];
      }
      /**
      * @param {User} user
      @returns void
      ***/
      addFollower(user) {
      this. followers.push(user);
      }
      /**
      * Get the followers who are tagged with tag
      @param {string} tag
      * @returns {Array.<User>}
      */
      getFollowers (tag) {
      // Fill in this line
      // return this.followers.filter(
      // (follower) => follower.tags.includes (tag));
  
      // return this. followers.includes (
      //     (follower) => follower.tags.filter(tag)
      //     );
  
  //     return this.followers.filter(
  // (follower) =>
  // follower.tags.filter((followerTag) => tag ===
  // followerTag
  // ).length > 0
  // );
  
  // return this.followers.map(
  // (follower) => follower.tags.includes(tag)
  // );
      }
      }
  
      let userObj = new User('a', ['1', '2', '3', '4', '5']);
      userObj.addFollower('b')
      console.log(userObj.getFollowers('2'));
  
      // tsc js-basics/ts-class.ts  
      // node js-basics/ts-class.js 
  