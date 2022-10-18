variable "es_version" {
  default = "8.4.3"
}

variable "env" {
  default = ""
}

## Elastic scale
variable "es_topologies" {
  type = list(object({
    type = string
    size_in_gb = string
    zones = number
  }))
}

variable "monitoring_deployment_id" {
  default = ""
}