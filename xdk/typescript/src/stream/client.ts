/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the Stream endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  StreamPostsFirehoseJaResponse,
  StreamGetRuleCountsResponse,
  StreamPostsSampleResponse,
  StreamPostsFirehoseEnResponse,
  StreamPostsFirehosePtResponse,
  StreamPostsFirehoseKoResponse,
  StreamLikesSample10Response,
  StreamGetRulesResponse,
  StreamUpdateRulesRequest,
  StreamUpdateRulesResponse,
  StreamLikesFirehoseResponse,
  StreamLikesComplianceResponse,
  StreamPostsComplianceResponse,
  StreamPostsResponse,
  StreamPostsSample10Response,
  StreamUsersComplianceResponse,
  StreamLabelsComplianceResponse,
  StreamPostsFirehoseResponse
} from "./models.js";

/**
 * Client for Stream operations
 */
export class StreamClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Stream Japanese Posts
     * Streams all public Japanese-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsFirehoseJaResponse Response data
     */
  async postsFirehoseJa(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsFirehoseJaResponse> {
    let url = this.client.baseUrl + "/2/tweets/firehose/stream/lang/ja";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsFirehoseJaResponse;
  }

  /**
     * Get stream rule counts
     * Retrieves the count of rules in the active rule set for the filtered stream.
     * @param rulesCountfields A comma separated list of RulesCount fields to display.* @returns StreamGetRuleCountsResponse Response data
     */
  async getRuleCounts(
    rulesCountfields?: Array<any>
  ): Promise<StreamGetRuleCountsResponse> {
    let url = this.client.baseUrl + "/2/tweets/search/stream/rules/counts";

    const params = new URLSearchParams();

    if (rulesCountfields !== undefined) {
      params.set("rules_count.fields", rulesCountfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamGetRuleCountsResponse;
  }

  /**
     * Stream sampled Posts
     * Streams a 1% sample of public Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsSampleResponse Response data
     */
  async postsSample(
    backfillMinutes?: number,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsSampleResponse> {
    let url = this.client.baseUrl + "/2/tweets/sample/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsSampleResponse;
  }

  /**
     * Stream English Posts
     * Streams all public English-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsFirehoseEnResponse Response data
     */
  async postsFirehoseEn(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsFirehoseEnResponse> {
    let url = this.client.baseUrl + "/2/tweets/firehose/stream/lang/en";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsFirehoseEnResponse;
  }

  /**
     * Stream Portuguese Posts
     * Streams all public Portuguese-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsFirehosePtResponse Response data
     */
  async postsFirehosePt(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsFirehosePtResponse> {
    let url = this.client.baseUrl + "/2/tweets/firehose/stream/lang/pt";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsFirehosePtResponse;
  }

  /**
     * Stream Korean Posts
     * Streams all public Korean-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsFirehoseKoResponse Response data
     */
  async postsFirehoseKo(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsFirehoseKoResponse> {
    let url = this.client.baseUrl + "/2/tweets/firehose/stream/lang/ko";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsFirehoseKoResponse;
  }

  /**
     * Stream sampled Likes
     * Streams a 10% sample of public Likes in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param likeWithTweetAuthorfields A comma separated list of LikeWithTweetAuthor fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns StreamLikesSample10Response Response data
     */
  async likesSample10(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    likeWithTweetAuthorfields?: Array<any>,
    expansions?: Array<any>,
    userfields?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<StreamLikesSample10Response> {
    let url = this.client.baseUrl + "/2/likes/sample10/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (likeWithTweetAuthorfields !== undefined) {
      params.set(
        "like_with_tweet_author.fields",
        likeWithTweetAuthorfields.map(String).join(",")
      );
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamLikesSample10Response;
  }

  /**
     * Get stream rules
     * Retrieves the active rule set or a subset of rules for the filtered stream.
     * @param ids A comma-separated list of Rule IDs.
     * @param maxResults The maximum number of results.
     * @param paginationToken This value is populated by passing the 'next_token' returned in a request to paginate through results.* @returns StreamGetRulesResponse Response data
     */
  async getRules(
    ids?: Array<any>,
    maxResults?: number,
    paginationToken?: string
  ): Promise<StreamGetRulesResponse> {
    let url = this.client.baseUrl + "/2/tweets/search/stream/rules";

    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.set("ids", ids.map(String).join(","));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamGetRulesResponse;
  }

  /**
     * Update stream rules
     * Adds or deletes rules from the active rule set for the filtered stream.
     * @param dryRun Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
     * @param deleteAll Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.* @param body Request body* @returns StreamUpdateRulesResponse Response data
     */
  async updateRules(
    body: StreamUpdateRulesRequest,
    dryRun?: boolean,
    deleteAll?: boolean
  ): Promise<StreamUpdateRulesResponse> {
    let url = this.client.baseUrl + "/2/tweets/search/stream/rules";

    const params = new URLSearchParams();

    if (dryRun !== undefined) {
      params.set("dry_run", String(dryRun));
    }

    if (deleteAll !== undefined) {
      params.set("delete_all", String(deleteAll));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    headers.set("Content-Type", "application/json");

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamUpdateRulesResponse;
  }

  /**
     * Stream all Likes
     * Streams all public Likes in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param likeWithTweetAuthorfields A comma separated list of LikeWithTweetAuthor fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns StreamLikesFirehoseResponse Response data
     */
  async likesFirehose(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    likeWithTweetAuthorfields?: Array<any>,
    expansions?: Array<any>,
    userfields?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<StreamLikesFirehoseResponse> {
    let url = this.client.baseUrl + "/2/likes/firehose/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (likeWithTweetAuthorfields !== undefined) {
      params.set(
        "like_with_tweet_author.fields",
        likeWithTweetAuthorfields.map(String).join(",")
      );
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamLikesFirehoseResponse;
  }

  /**
     * Stream Likes compliance data
     * Streams all compliance data related to Likes for Users.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided.* @returns StreamLikesComplianceResponse Response data
     */
  async likesCompliance(
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string
  ): Promise<StreamLikesComplianceResponse> {
    let url = this.client.baseUrl + "/2/likes/compliance/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamLikesComplianceResponse;
  }

  /**
     * Stream Posts compliance data
     * Streams all compliance data related to Posts.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.* @returns StreamPostsComplianceResponse Response data
     */
  async postsCompliance(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string
  ): Promise<StreamPostsComplianceResponse> {
    let url = this.client.baseUrl + "/2/tweets/compliance/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsComplianceResponse;
  }

  /**
     * Stream filtered Posts
     * Streams Posts in real-time matching the active rule set.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsResponse Response data
     */
  async posts(
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsResponse> {
    let url = this.client.baseUrl + "/2/tweets/search/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsResponse;
  }

  /**
     * Stream 10% sampled Posts
     * Streams a 10% sample of public Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsSample10Response Response data
     */
  async postsSample10(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsSample10Response> {
    let url = this.client.baseUrl + "/2/tweets/sample10/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsSample10Response;
  }

  /**
     * Stream Users compliance data
     * Streams all compliance data related to Users.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.* @returns StreamUsersComplianceResponse Response data
     */
  async usersCompliance(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string
  ): Promise<StreamUsersComplianceResponse> {
    let url = this.client.baseUrl + "/2/users/compliance/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamUsersComplianceResponse;
  }

  /**
     * Stream Post labels
     * Streams all labeling events applied to Posts.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.* @returns StreamLabelsComplianceResponse Response data
     */
  async labelsCompliance(
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string
  ): Promise<StreamLabelsComplianceResponse> {
    let url = this.client.baseUrl + "/2/tweets/label/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamLabelsComplianceResponse;
  }

  /**
     * Stream all Posts
     * Streams all public Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns StreamPostsFirehoseResponse Response data
     */
  async postsFirehose(
    partition: number,
    backfillMinutes?: number,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<StreamPostsFirehoseResponse> {
    let url = this.client.baseUrl + "/2/tweets/firehose/stream";

    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set("backfill_minutes", String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set("partition", String(partition));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request using the HTTP client
    const response = await this.client.httpClient.request(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as StreamPostsFirehoseResponse;
  }
}
