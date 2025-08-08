/**
 * Aaasubscriptions client for the X API.
 *
 * This module provides a client for interacting with the Aaasubscriptions endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  AaasubscriptionsCreateAccountActivitySubscriptionRequest,
  AaasubscriptionsCreateAccountActivitySubscriptionResponse
} from "./models.js";

/**
 * Client for Aaasubscriptions operations
 */
export class AaasubscriptionsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Create subscription
     * Creates an Account Activity subscription for the user and the given webhook.
     * @param webhookId The webhook ID to check subscription against.* @param body Request body* @returns AaasubscriptionsCreateAccountActivitySubscriptionResponse Response data
     */
  async createAccountActivitySubscription(
    webhookId: string,
    body?: AaasubscriptionsCreateAccountActivitySubscriptionRequest
  ): Promise<AaasubscriptionsCreateAccountActivitySubscriptionResponse> {
    let url =
      this.client.baseUrl +
      "/2/account_activity/webhooks/{webhook_id}/subscriptions/all";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{webhook_id}", String(webhookId));

    const headers = new Headers();

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
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

    return responseData as AaasubscriptionsCreateAccountActivitySubscriptionResponse;
  }
}
