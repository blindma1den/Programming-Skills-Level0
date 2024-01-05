const user = {
    username: "nysterr",
    password: "123456",
    balance: 2000,
  };
  
  const user2 = {
    username: "other",
    password: "123456",
    balance: 500,
  };
  
  //Login
  
  let attempts = 3;
  
  const login = (username: string, password: string) => {
    if (attempts === 0) {
      return {
        blocked: "You've been blocked for failed attempts",
      };
    }
  
    if (username !== user.username || password !== user.password) {
      attempts--;
      return {
        error: "Credentials not valid",
      };
    }
  
    return { success: true };
  };
  
  
  const deposit = (amount: number) => {
    if (amount <= 0 || amount === undefined) {
      return "You do not have enough money";
    }
  
    return user.balance + amount;
  };
  
  const withdraw = (amount: number, origin) => {
    if (amount <= 0 || amount === undefined) {
      return "You do not have enough money";
    }
  
    if (amount > origin.balance) {
      return "You do not have enough money";
    }
  
    return user.balance - amount;
  };
  
  const viewBalance = () => {
    return user.balance;
  };
  
  const transfer = (amount: number, origin, destiny) => {
    if (amount <= 0 || amount === undefined) {
      return "Please, the amount must be a number greater than 0";
    }
  
    if (amount > origin.balance) {
      return "You do not have enough money";
    }
  
    const totalBalance = origin.balance - amount;
    const moneySent = destiny.balance + amount;
  
    return {
      totalBalance,
      moneySent,
    };
  };
  
  const menu = (user) => {
    return {
      balance: user.balance,
      deposit,
      transfer,
    };
  };
  