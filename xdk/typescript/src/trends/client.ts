/**
 * Trends client for the X API.
 *
 * This module provides a client for interacting with the Trends endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  TrendsGetUsersPersonalizedResponse,
  TrendsGetByWoeidResponse
} from "./models.js";

/**
 * Client for Trends operations
 */
export class TrendsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get personalized Trends
     * Retrieves personalized trending topics for the authenticated user.
     * @param personalizedTrendfields A comma separated list of PersonalizedTrend fields to display.* @returns TrendsGetUsersPersonalizedResponse Response data
     */
  async getUsersPersonalized(
    personalizedTrendfields?: Array<any>
  ): Promise<TrendsGetUsersPersonalizedResponse> {
    let url = this.client.baseUrl + "/2/users/personalized_trends";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (personalizedTrendfields !== undefined) {
      params.set(
        "personalized_trend.fields",
        personalizedTrendfields.map(String).join(",")
      );
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
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

    return responseData as TrendsGetUsersPersonalizedResponse;
  }

  /**
     * Get Trends by WOEID
     * Retrieves trending topics for a specific location identified by its WOEID.
     * @param woeid The WOEID of the place to lookup a trend for.
     * @param maxTrends The maximum number of results.
     * @param trendfields A comma separated list of Trend fields to display.* @returns TrendsGetByWoeidResponse Response data
     */
  async getByWoeid(
    woeid: number,
    maxTrends?: number,
    trendfields?: Array<any>
  ): Promise<TrendsGetByWoeidResponse> {
    let url = this.client.baseUrl + "/2/trends/by/woeid/{woeid}";

    const params = new URLSearchParams();

    if (maxTrends !== undefined) {
      params.set("max_trends", String(maxTrends));
    }

    if (trendfields !== undefined) {
      params.set("trend.fields", trendfields.map(String).join(","));
    }

    url = url.replace("{woeid}", String(woeid));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
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

    return responseData as TrendsGetByWoeidResponse;
  }
}
