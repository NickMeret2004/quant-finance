#include <bits/stdc++.h>        //convenience strings, vectors, iostream (bits folder name)...
#include <curl/curl.h>          //libcrul library: HTTP requests and other netwrok requests
#include <nlohann/json.hpp>     //JSON Library, parsing >> C++ (header-only library)

using json = nlohmann::json;

static size_t writeToString(void* contents, size_t size, size_t nmemb, void* userp) {
    size_t realSize = size * nmemb;
    auto* buffer = static_cast<std::string*>(userp);
    buffer->append(static_cast<char*>(contents), realSize);
    return realSize;
}

int main() {
    std::cout << "Build OK. We'll wire the rest next.\n";
    return 0;
}
