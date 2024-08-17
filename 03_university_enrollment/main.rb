
programs = {
    cs: 0 ,
    medine: 1,
    marketing: 0,
    arts: 3
}

puts "Username :"
username = gets.chomp
puts "Password: "
password = gets.chomp

if username == "admin" && password == "admin"
    puts "Chose the program you want"
    puts "1. Computer Science"
    puts "2. Medicine"
    puts "3. Marketing"
    puts "4. Arts"
    
    choice = gets.chomp
    puts choice
    puts choice.class
    case  choice
        when "1"
            if programs[:cs] == 0
                puts "Sin expacios disponibles"
            else
                puts programs[:cs] = programs[:cs] - 1 
            end 
        when "2"

    end
    puts  programs

   # Computer Science, Medicine, Marketing, and Arts.
else
    puts "Invalid username or password"
end