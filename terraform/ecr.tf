resource "aws_ecr_repository" "app" {

  name = "micro1-devops"

  image_scanning_configuration {
    scan_on_push = true
  }

  image_tag_mutability = "MUTABLE"
}
