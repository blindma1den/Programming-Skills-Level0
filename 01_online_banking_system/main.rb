=begin
1. Create an online banking system with the following features:

1.1 Users must be able to log in with a username and password.
1.2 If the user enters the wrong credentials three times, the system must lock them out.
2.0 The initial balance in the bank account is $2000.
2.1 The system must allow users to deposit, withdraw, view, and transfer money.
2.2 The system must display a menu for users to perform transactions.  
=end



number_attemps = 0;
validPassword = "123"
validUsername = "batman"
initialValance = 2000
flag = true

max_attemps = 3
   
    loop do
        print "What is your username? "
        username = gets.chomp
        print "What is your password? "
        password = gets.chomp

        if  password == validPassword && username == validUsername
            
            loop do

                puts "Welcome"
                puts "1.Deposit"
                puts "2.withdraw"
                puts "3. view"
                puts "4. transfer"
                puts "5. exit"
                
                option = gets.chomp.to_i
                    if option == 1
                        puts "Insert the ammount to insert"
                        ammount = gets.chomp
                        initialValance += ammount.to_i
                       
                    elsif option == 2
                        puts "insert the amount to withdraw"
                        withdraw = gets.chomp
                        initialValance -= withdraw.to_i
                    elsif option == 3
                        puts "Your total is #{initialValance}"
                    elsif option == 4
                        puts "Account to transfer: "
                        account = gets.chomp
                        puts "Amount to transfer: "
                        amount = gets.chomp
                        initialValance -= amount.to_i

                    elsif option == 5
                        print "THANKS FOR USING OUR SERVICES"
                        flagExit = false
                        flag = false
                            
                    end
                break if option == 5
            
            end
           
        else 
            number_attemps +=1
        end
        break if max_attemps == number_attemps
       
    end