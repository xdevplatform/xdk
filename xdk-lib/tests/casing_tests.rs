use xdk_lib::Casing;

#[test]
fn test_casing_enum_convert_words() {
    let words = vec!["hello".to_string(), "world".to_string()];

    assert_eq!(Casing::Snake.convert_words(&words), "hello_world");
    assert_eq!(Casing::Pascal.convert_words(&words), "HelloWorld");
    assert_eq!(Casing::Camel.convert_words(&words), "helloWorld");
    assert_eq!(Casing::Kebab.convert_words(&words), "hello-world");
    assert_eq!(Casing::ScreamingSnake.convert_words(&words), "HELLO_WORLD");
}

#[test]
fn test_casing_enum_single_word() {
    let words = vec!["user".to_string()];

    assert_eq!(Casing::Snake.convert_words(&words), "user");
    assert_eq!(Casing::Pascal.convert_words(&words), "User");
    assert_eq!(Casing::Camel.convert_words(&words), "user");
    assert_eq!(Casing::Kebab.convert_words(&words), "user");
    assert_eq!(Casing::ScreamingSnake.convert_words(&words), "USER");
}

#[test]
fn test_casing_enum_empty_words() {
    let words: Vec<String> = vec![];

    assert_eq!(Casing::Snake.convert_words(&words), "");
    assert_eq!(Casing::Pascal.convert_words(&words), "");
    assert_eq!(Casing::Camel.convert_words(&words), "");
    assert_eq!(Casing::Kebab.convert_words(&words), "");
    assert_eq!(Casing::ScreamingSnake.convert_words(&words), "");
}

#[test]
fn test_casing_enum_complex_words() {
    let words = vec![
        "get".to_string(),
        "user".to_string(),
        "profile".to_string(),
        "data".to_string(),
    ];

    assert_eq!(Casing::Snake.convert_words(&words), "get_user_profile_data");
    assert_eq!(Casing::Pascal.convert_words(&words), "GetUserProfileData");
    assert_eq!(Casing::Camel.convert_words(&words), "getUserProfileData");
    assert_eq!(Casing::Kebab.convert_words(&words), "get-user-profile-data");
    assert_eq!(
        Casing::ScreamingSnake.convert_words(&words),
        "GET_USER_PROFILE_DATA"
    );
}

#[test]
fn test_casing_enum_mixed_case_words() {
    // Test with already cased words
    let words = vec!["getUserID".to_string()];

    assert_eq!(Casing::Snake.convert_words(&words), "getuserid");
    assert_eq!(Casing::Pascal.convert_words(&words), "GetUserID");
    assert_eq!(Casing::Camel.convert_words(&words), "getuserid");
    assert_eq!(Casing::Kebab.convert_words(&words), "getuserid");
    assert_eq!(Casing::ScreamingSnake.convert_words(&words), "GETUSERID");
}

#[test]
fn test_casing_enum_special_characters() {
    // Test with words containing special characters
    let words = vec!["hello_world".to_string()];

    assert_eq!(Casing::Snake.convert_words(&words), "hello_world");
    assert_eq!(Casing::Pascal.convert_words(&words), "HelloWorld");
    assert_eq!(Casing::Camel.convert_words(&words), "hello_world");
    assert_eq!(Casing::Kebab.convert_words(&words), "hello_world");
    assert_eq!(Casing::ScreamingSnake.convert_words(&words), "HELLO_WORLD");
}

#[test]
fn test_casing_enum_numbers() {
    let words = vec!["user".to_string(), "v2".to_string(), "api".to_string()];

    assert_eq!(Casing::Snake.convert_words(&words), "user_v2_api");
    assert_eq!(Casing::Pascal.convert_words(&words), "UserV2Api");
    assert_eq!(Casing::Camel.convert_words(&words), "userV2Api");
    assert_eq!(Casing::Kebab.convert_words(&words), "user-v2-api");
    assert_eq!(Casing::ScreamingSnake.convert_words(&words), "USER_V2_API");
}

#[test]
fn test_casing_enum_real_world_examples() {
    // Test with real operation names that would be used in practice
    let get_user_profile = vec!["get".to_string(), "user".to_string(), "profile".to_string()];

    assert_eq!(
        Casing::Snake.convert_words(&get_user_profile),
        "get_user_profile"
    );
    assert_eq!(
        Casing::Pascal.convert_words(&get_user_profile),
        "GetUserProfile"
    );
    assert_eq!(
        Casing::Camel.convert_words(&get_user_profile),
        "getUserProfile"
    );
    assert_eq!(
        Casing::Kebab.convert_words(&get_user_profile),
        "get-user-profile"
    );
    assert_eq!(
        Casing::ScreamingSnake.convert_words(&get_user_profile),
        "GET_USER_PROFILE"
    );

    // Test tag names
    let community_notes = vec!["community".to_string(), "notes".to_string()];

    assert_eq!(
        Casing::Snake.convert_words(&community_notes),
        "community_notes"
    );
    assert_eq!(
        Casing::Pascal.convert_words(&community_notes),
        "CommunityNotes"
    );
    assert_eq!(
        Casing::Camel.convert_words(&community_notes),
        "communityNotes"
    );
    assert_eq!(
        Casing::Kebab.convert_words(&community_notes),
        "community-notes"
    );
    assert_eq!(
        Casing::ScreamingSnake.convert_words(&community_notes),
        "COMMUNITY_NOTES"
    );
}

#[test]
fn test_casing_enum_copy_clone() {
    let casing = Casing::Pascal;
    let casing_copy = casing;
    let casing_clone = casing.clone();

    let words = vec!["test".to_string()];

    assert_eq!(casing.convert_words(&words), "Test");
    assert_eq!(casing_copy.convert_words(&words), "Test");
    assert_eq!(casing_clone.convert_words(&words), "Test");
}

#[test]
fn test_casing_enum_convert_string() {
    // Test converting camelCase strings
    assert_eq!(Casing::Snake.convert_string("maxResults"), "max_results");
    assert_eq!(Casing::Pascal.convert_string("maxResults"), "MaxResults");
    assert_eq!(Casing::Camel.convert_string("maxResults"), "maxResults");
    assert_eq!(Casing::Kebab.convert_string("maxResults"), "max-results");
    assert_eq!(Casing::ScreamingSnake.convert_string("maxResults"), "MAX_RESULTS");

    // Test converting PascalCase strings
    assert_eq!(Casing::Snake.convert_string("GetUserProfile"), "get_user_profile");
    assert_eq!(Casing::Pascal.convert_string("GetUserProfile"), "GetUserProfile");
    assert_eq!(Casing::Camel.convert_string("GetUserProfile"), "getUserProfile");
    assert_eq!(Casing::Kebab.convert_string("GetUserProfile"), "get-user-profile");
    assert_eq!(Casing::ScreamingSnake.convert_string("GetUserProfile"), "GET_USER_PROFILE");

    // Test converting snake_case strings
    assert_eq!(Casing::Snake.convert_string("user_id"), "user_id");
    assert_eq!(Casing::Pascal.convert_string("user_id"), "UserId");
    assert_eq!(Casing::Camel.convert_string("user_id"), "userId");
    assert_eq!(Casing::Kebab.convert_string("user_id"), "user-id");
    assert_eq!(Casing::ScreamingSnake.convert_string("user_id"), "USER_ID");

    // Test converting kebab-case strings  
    assert_eq!(Casing::Snake.convert_string("user-profile"), "user_profile");
    assert_eq!(Casing::Pascal.convert_string("user-profile"), "UserProfile");
    assert_eq!(Casing::Camel.convert_string("user-profile"), "userProfile");
    assert_eq!(Casing::Kebab.convert_string("user-profile"), "user-profile");
    assert_eq!(Casing::ScreamingSnake.convert_string("user-profile"), "USER_PROFILE");
}

#[test]
fn test_casing_enum_debug() {
    let casing = Casing::Pascal;
    let debug_string = format!("{:?}", casing);
    assert_eq!(debug_string, "Pascal");
}
