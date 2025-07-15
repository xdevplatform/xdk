use xdk_gen::python::generator::strip_resource_name;

fn main() {
    // Test cases from the actual OpenAPI spec
    println!("Testing strip_resource_name function:");
    println!();
    
    // Communities
    println!("searchCommunities (/2/communities/search) -> {}", 
             strip_resource_name("/2/communities/search", "searchCommunities"));
    
    // Posts (tweets)
    println!("createPosts (/2/tweets) -> {}", 
             strip_resource_name("/2/tweets", "createPosts"));
    println!("getPostsById (/2/tweets/{id}) -> {}", 
             strip_resource_name("/2/tweets/{id}", "getPostsById"));
    println!("searchPostsAll (/2/tweets/search/all) -> {}", 
             strip_resource_name("/2/tweets/search/all", "searchPostsAll"));
    
    // Users
    println!("getUsersById (/2/users/{id}) -> {}", 
             strip_resource_name("/2/users/{id}", "getUsersById"));
    println!("searchUsers (/2/users/search) -> {}", 
             strip_resource_name("/2/users/search", "searchUsers"));
    
    // Account Activity
    println!("createAccountActivityReplayJob (/2/account_activity/replay) -> {}", 
             strip_resource_name("/2/account_activity/replay", "createAccountActivityReplayJob"));
} 