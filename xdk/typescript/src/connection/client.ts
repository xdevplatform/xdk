/**
 * Connection client for the X API.
 *
 * This module provides a client for interacting with the Connection endpoints of the X API.
 */

import { Client } from "../client.js";
import { ConnectionDeleteAllResponse } from "./models.js";

/**
 * Client for Connection operations
 */
export class ConnectionClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Terminate all connections
     * Terminates all active streaming connections for the authenticated application.* @returns ConnectionDeleteAllResponse Response data
     */
  async deleteAll(): Promise<ConnectionDeleteAllResponse> {
    let url = this.client.baseUrl + "/2/connections/all";

    const params = new URLSearchParams();

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
        method: "DELETE",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as ConnectionDeleteAllResponse;
  }
}
