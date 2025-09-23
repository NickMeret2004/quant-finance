Brownian Motion CPP


Objectives:

Pull real stock price data from Alpha vantage API

Parse the JSON response into usable data

Calculate log returns from the prices

Estimate drift and volatility front those returns

Plug them into Geometric Brownian Motion equation

Output the terms clearly (drift, diffusion, simulated ds, etc)





Code Segment 1(writing received HTTP data chunks into a string buffer):

	Function static size_t  writeToString: Static function has internal linkage, other files wont be able to use this info.

	Size_t: type, used to represent size of memory, given by the standard library.


	Parameters: 
void* contents (pointer to data we are receiving, doesn't know specific type of data yet.)

Size_t size (tells us how large each piece of the data is in bytes)

Size_t nmemb (number of elements in data, to multiply by size, in library (lib curl) calculates and provides itself)

void* userp ( pointer without type yet, pass in a user defined data structure, place holder to pass any type of data wanted, we are using to pass a pointer into a standard string)




Line by line explanation: 
	auto* buffer = static_cast<std::string*>(userp); (compiler figures out type of pointer called buffer, turning pointer userp into a string pointer, and passing that into buffer)

	buffer->append(static_cast<char*>(contents), realSize); (buffer is a temporary storage area in memory because we need a place to store each chunk of data before we have all data collected, turning contents into char pointer, then appending data into buffer, real size is the number of bytes we are appending).

	return realSize; (telling function to give back the number of bytes that we appended to the buffer).
