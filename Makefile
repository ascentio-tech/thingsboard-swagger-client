SWAGGER_VERSION=3.0.20
swagger-codegen-cli.jar:
	wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/${SWAGGER_VERSION}/swagger-codegen-cli-${SWAGGER_VERSION}.jar -O swagger-codegen-cli.jar

THINGSBOARD_VERSION=2.3.0
clean-generated:
	rm -rf docs thingsboard_client
clean:
	rm -rf dist
.PHONY: clean clean-generated

SWAGGER_SPEC=swagger/thingsboard.json
clean-swagger-spec:
	sed -i -e 's/{?.*}//g' ${SWAGGER_SPEC}
	sed -i -e '/"isPublic"$$/d' ${SWAGGER_SPEC}

generate-swagger-client: swagger-codegen-cli.jar clean-swagger-spec clean-generated
	java -jar swagger-codegen-cli.jar generate -i ${SWAGGER_SPEC} -l python -o . \
    --additional-properties projectName=thingsboard-swagger-client,packageName=thingsboard_client,packageVersion=${THINGSBOARD_VERSION},appDescription='Thingsboard REST client (auto-generated from Swagger spec)'

dist/thingsboard-swagger-client-${THINGSBOARD_VERSION}.tar.gz:
	python setup.py sdist

install-swagger-client: dist/thingsboard-swagger-client-${THINGSBOARD_VERSION}.tar.gz
	pip install dist/*${THINGSBOARD_VERSION}.tar.gz

