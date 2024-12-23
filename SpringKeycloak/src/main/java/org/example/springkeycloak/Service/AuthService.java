package org.example.springkeycloak.Service;

import org.example.springkeycloak.DTO.RegisterDTO;
import org.jboss.resteasy.client.jaxrs.ResteasyClientBuilder;
import org.keycloak.OAuth2Constants;
import org.keycloak.admin.client.Keycloak;
import org.keycloak.admin.client.KeycloakBuilder;
import org.keycloak.admin.client.resource.RealmResource;
import org.keycloak.admin.client.resource.UserResource;
import org.keycloak.admin.client.resource.UsersResource;
import org.keycloak.representations.idm.CredentialRepresentation;
import org.keycloak.representations.idm.UserRepresentation;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;


import javax.ws.rs.core.Response;
import java.util.*;
import java.util.logging.Logger;

@Service
public class AuthService {
    private final String CLIENT_ID = "Flutter-Client";
    private final String CLIENT_SECRET = "gran";
    private final String KEYCLOAK_TOKEN_URL = "http://localhost:8180/realms/OCR-Realm/protocol/openid-connect/token";
    private static final String REALM = "OCR-Realm";
    Logger logger = Logger.getLogger(AuthService.class.getName());

    public Map<String, Object> registerUser(RegisterDTO registerDTO) {
        logger.info("Registering user: " + registerDTO.getUsername());
        logger.info("Registering user: " + registerDTO.getPassword());
        logger.info("Registering user: " + registerDTO.getEmail());
        try {
            RestTemplate restTemplate = new RestTemplate();

            // Step 1: Get admin token
            HttpHeaders tokenHeaders = new HttpHeaders();
            tokenHeaders.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

            MultiValueMap<String, String> tokenRequest = new LinkedMultiValueMap<>();
            tokenRequest.add("client_id", "Client_OCR");
            tokenRequest.add("client_secret", "N30o8iKRwEKd2I7H6ClofRNfE4nx1VLR");
            tokenRequest.add("grant_type", "client_credentials");

            HttpEntity<MultiValueMap<String, String>> tokenEntity = new HttpEntity<>(tokenRequest, tokenHeaders);

            ResponseEntity<Map> tokenResponse = restTemplate.exchange(
                    "http://localhost:8180/realms/OCR-Realm/protocol/openid-connect/token",
                    HttpMethod.POST,
                    tokenEntity,
                    Map.class
            );

            if (!tokenResponse.getStatusCode().is2xxSuccessful()) {
                throw new RuntimeException("Failed to fetch admin token.");
            }

            String accessToken = (String) tokenResponse.getBody().get("access_token");

            // Step 2: Use the token to create a new user
            HttpHeaders userHeaders = new HttpHeaders();
            userHeaders.setContentType(MediaType.APPLICATION_JSON);
            userHeaders.setBearerAuth(accessToken);

            Map<String, Object> userPayload = new HashMap<>();
            userPayload.put("enabled", true);
            userPayload.put("username", registerDTO.getUsername());
            userPayload.put("firstName", "first name");
            userPayload.put("email", registerDTO.getEmail());
            userPayload.put("emailVerified", true);

            List<Map<String, Object>> credentials = new ArrayList<>();
            Map<String, Object> credential = new HashMap<>();
            credential.put("type", "password");
            credential.put("value", registerDTO.getPassword());
            credential.put("temporary", false);
            credentials.add(credential);

            userPayload.put("credentials", credentials);

            HttpEntity<Map<String, Object>> userEntity = new HttpEntity<>(userPayload, userHeaders);

            ResponseEntity<Map> userResponse = restTemplate.exchange(
                    "http://localhost:8180/admin/realms/OCR-Realm/users",
                    HttpMethod.POST,
                    userEntity,
                    Map.class
            );

            if (!userResponse.getStatusCode().is2xxSuccessful()) {
                throw new RuntimeException("Failed to create user.");
            }

            // Return success response
            Map<String, Object> result = new HashMap<>();
            result.put("status", HttpStatus.CREATED);
            result.put("message", "User successfully created.");
            result.put("data", userResponse.getBody());
            return result;

        } catch (Exception e) {
            // Handle errors
            Map<String, Object> errorResponse = new HashMap<>();
            errorResponse.put("status", HttpStatus.INTERNAL_SERVER_ERROR);
            errorResponse.put("error", e.getMessage());
            return errorResponse;
        }
    }

    public Map<String, Object> register(RegisterDTO registerDTO) {
        logger.info("Registering user: " + registerDTO.getUsername());
        logger.info("Registering user: " + registerDTO.getPassword());
        Keycloak keycloak = KeycloakBuilder.builder()
                .serverUrl("http://localhost:8180/auth")
                .realm(REALM)
                .grantType(OAuth2Constants.CLIENT_CREDENTIALS)
                .clientId(CLIENT_ID)
                .clientSecret(CLIENT_SECRET)
                .build();
        UserRepresentation user = new UserRepresentation();
        user.setEnabled(true);
        user.setUsername(registerDTO.getUsername());
        user.setEmail(registerDTO.getEmail());
        user.setFirstName("John");
        user.setLastName("Doe");

        CredentialRepresentation credential = new CredentialRepresentation();
        credential.setTemporary(false);
        credential.setType(CredentialRepresentation.PASSWORD);
        credential.setValue(registerDTO.getPassword());

        user.setCredentials(Collections.singletonList(credential));

        RealmResource realmResource = keycloak.realm(REALM);
        UsersResource usersResource = realmResource.users();
        Response response = usersResource.create(user);

        if (response.getStatus() != 201) {
            logger.info("Failed to create user: " + response.getStatus());
            logger.info("Reason: " + response.getStatusInfo());
            throw new RuntimeException("Failed to create user");
        }

        Map<String, Object> result = new HashMap<>();
        result.put("status", HttpStatus.CREATED);
        result.put("message", "User created successfully");
        return result;
    }

}