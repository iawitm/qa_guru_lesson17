get_single_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "email": {
      "type": "string"
    },
    "first_name": {
      "type": "string"
    },
    "last_name": {
      "type": "string"
    },
    "avatar": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "email",
    "first_name",
    "last_name",
    "avatar"
  ]
}

post_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "id",
    "createdAt"
  ]
}

put_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "updatedAt"
  ]
}

get_single_resource = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "year": {
      "type": "integer"
    },
    "color": {
      "type": "string"
    },
    "pantone_value": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "year",
    "color",
    "pantone_value"
  ]
}

error = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}