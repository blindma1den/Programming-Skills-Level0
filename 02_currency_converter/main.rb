percentageAverage = 1
isFinishProgram = 0

def print_menu(title)
	puts title
	puts "CLP"
	puts "ARS"
	puts "USD"
	puts "EUR"
	puts "TRY"
	puts "GBP"
end

def data_insert_to_number
	return gets.chomp.to_i
end

def calculateExchange (amount, value) 
	puts amount 
	puts value
	return amount * value 
end

def calculateCommision(percentageAverage, exchange)
	return (( percentageAverage * exchange) / 100 	).round	
end


curencies = {
	"CLP" => 12.21,
	"ARG" =>9,
	"USD" => 12,
	"EUR" => 1.50,
	"TRY" => 221,
	"GBP" => 2
} 

until isFinishProgram == 1

	puts "**** WELCOME****"
	puts "Insert the amount to convert: "
	amount = data_insert_to_number

	print_menu("Select your currency ")
	currency = gets.chomp

	print_menu("Select the currenct to exchange: ")
	currencyToExchange = gets.chomp

	exchange = calculateExchange(amount, curencies[currency])

	puts exchange
	puts "The exchange from #{currency} to #{currencyToExchange} is #{exchange}"
	puts "Do you want to withdraw the funds?"
	puts "1. Yes" 
	puts "2. No"

	isWithdraw = gets.chomp

	if isWithdraw == 1

		total =calculateCommision(percentageAverage, )
		puts total
	else 
		puts "Do you want to perform another operation?"
		puts "1. Yes" 
		puts "2. No"
		isExit = gets.chomp
		if isExit == "2"
			puts "Thanks"
			isFinishProgram = 1
		end
	end
end